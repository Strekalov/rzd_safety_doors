import Vue from 'vue'
import Vuetify from 'vuetify/lib'

Vue.use(Vuetify)

const vuetify = new Vuetify({
  theme: {
    themes: {
      light: {
        primary: '#2b2e4a',
        green: '#29bb89',
        secondary: '#e84545',
        anchor: '#8c9eff',
      },
    },
  },
})

export default vuetify