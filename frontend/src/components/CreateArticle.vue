<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p class="title is-1">Welcome to <span class="title-color"> Darticle </span> </p>
    <p class="subtitle is-3">Secure, anonymous, and open-source article platform</p>
    <section class="section is-small">
      <button class="button is-link is-light">Upload Your Author Key</button>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'CreateDarticle',
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
      setTimeout(() => loadingComponent.close(), 2 * 1000)
      const response = await axios.get('http://localhost:8000/article/create-author/')
      this.authorKey = response.data.author
      this.readerKey = response.data.reader
    },
    copyKeys () {
      let authKeyCombo = this.authorKey + '\n\n\n' + this.readerKey
      navigator.clipboard.writeText(authKeyCombo)
      const data = authKeyCombo
      const blob = new Blob([data], {type: 'text/plain'})
      const e = document.createEvent('MouseEvents')
      let a = document.createElement('a')
      a.download = 'darticle-key.txt'
      a.href = window.URL.createObjectURL(blob)
      a.dataset.downloadurl = ['text', a.download, a.href].join(':')
      e.initEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null)
      a.dispatchEvent(e)
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
