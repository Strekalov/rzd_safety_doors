<template>
  
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark>
    <v-card color="primary" flat>


    <v-toolbar-title style="font-size: 20">Система мониторинга безопасной посадки пассажиров</v-toolbar-title>
    <v-spacer></v-spacer>
    </v-card> 
    <template v-if="isConfig === false">
    <v-tabs right>
          <v-tabs-slider color="green"></v-tabs-slider>
          <v-tab @click="isConfig = !isConfig">Настройки</v-tab>
    </v-tabs>
    </template>
    <template v-else >
    <v-tabs right>
          <v-tabs-slider color="green"></v-tabs-slider>
          <v-tab @click="isConfig = !isConfig"> На главную</v-tab>
    </v-tabs>
    </template>



    <!-- <template v-else>
    <v-tabs right>
          <v-tabs-slider color="yellow"></v-tabs-slider>
          <v-tab>Настройки</v-tab>
    </v-tabs>
    </template> -->

    </v-app-bar>
    <template v-if="isConfig === false">
      <MainPage/>
    </template>
    <template v-else>
      <ConfigPage/>
    </template>
    
  </v-app>
</template>

<script>
// import ConfigService from './components/ConfigService';
// import ConfigBlacklist from './components/ConfigBlacklist';
// import ConfigTelegram from './components/ConfigTelegram';
import ConfigPage from './components/ConfigPage';
import MainPage from './components/MainPage';


export default {
  name: 'App',
  components: {
    MainPage,
    ConfigPage,
  },

  data: () => ({
    isConfig: false,
    config : {
      tolerance: "",
      blacklist_tolerance: "",
      blacklist_starttime: "",
      blacklist_stoptime: "",
      is_double_screen: false,
      blacklist: [],
      telegram: {
        chat_list: []
      }

    }
  }),
  methods: {
    toggleConfigs() {
        this.isConfig =! this.isConfig;
      }
  },

};
</script>
