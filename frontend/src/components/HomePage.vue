<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p class="title is-1">Welcome to <span class="title-color"> Darticle </span> </p>
    <p class="subtitle is-3">Secure, anonymous, and open-source article platform</p>
    <b-button @click="createAuthor" type="is-link">Generate Author PIN</b-button>
    <section class="section is-small">
      <b-notification class="mw-10" v-if="authorKey" ref="element" :closable="true">
      Author: {{authorKey| truncate(40, '...')}}<br>
      Reader: {{readerKey| truncate(40, '...')}}<br>
      <b-button @click="copyKeys" type="is-danger">
                Download Key
            </b-button>
    </b-notification>
    </section>
    <b-button @click="createAuthor" type="is-success">Write Article</b-button>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'HomePage',
  data () {
    return {
      msg: 'a project by @sepkimmy',
      isFullPage: true,
      authorKey: '',
      readerKey: ''
    }
  },
  methods: {
    async createAuthor () {
      const loadingComponent = this.$buefy.loading.open({
        container: this.isFullPage ? null : this.$refs.element.$el
      })
      setTimeout(() => loadingComponent.close(), 3 * 1000)
      const response = await axios.get('http://localhost:8000/article/create-author/')
      this.authorKey = response.data.author
      this.readerKey = response.data.reader
    },
    copyKeys () {
      let authKeyCombo = this.authorKey + this.readerKey
      navigator.clipboard.writeText(authKeyCombo)
      authKeyCombo = ''
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
