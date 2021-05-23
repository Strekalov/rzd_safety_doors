<template>
<div id="app">
  
<v-content>
    <v-container fill-height fluid>
  <v-row align="center"
      justify="center" class="mt-10 mb-10 pt10 pb10">
      <v-col cols="4" sm="6" md="4" lg="4">
          <v-btn color="green" block @click="postStartAnalisis">Запустить анализ стереокамер!</v-btn>
    </v-col>
    <v-alert v-if="status != 'success'" type="error" :value="alert">
            Ошибка при отправке запроса!
          </v-alert>
  </v-row>
</v-container>

    </v-content>
    <v-overlay :value="overlay">
    <div>
        <template v-if="cameras.length > 0">
  <v-overlay :value="overlay">
  <v-container fluid>
    
    <v-data-iterator
      :items="cameras"
      :items-per-page.sync="itemsPerPage"
      hide-default-footer
    >
      <template v-slot:header>
        <v-toolbar
          class="mb-2"
          color="secondary darken-5"
          dark
          flat
        >
          <v-toolbar-title>Внимание! Обнаружено застревание в двери поезда на камерах:</v-toolbar-title>
        </v-toolbar>
      </template>

      <template v-slot:default="props">
        <v-row align="center"
      justify="center">
          <v-col
            v-for="item in props.items"
            :key="item.name"
            cols="12"
            sm="12"
            md="8"
            lg="8"
          >
            <v-card>
              <v-card-title class="subheading font-weight-bold">
                {{ item.camera_title }}
              </v-card-title>

              <v-divider></v-divider>
                <v-list-item >

                <v-img :src="`${item.camera_screen}`" alt=""
                    contain   
                    height="400px"
                    width="400px">
                </v-img>

                </v-list-item>

            </v-card>
          </v-col>
        </v-row>
      </template>

    </v-data-iterator>
    
  </v-container>
  </v-overlay>
</template>
  </div>
  </v-overlay>


</div>
    
</template>





<script>
import BACKEND_URL from '../urls';
import axios from 'axios';


export default {
  name: "MainPage",
  props: ["config"],
  data: () => ({
    alert: false,
    status: '',
    cameras: [],
    itemsPerPage: 20,
    overlay: false
  }),
  methods: {
    postStartAnalisis: function() {
      this.overlay = true
      axios({
        url: `${BACKEND_URL}/v0/analysis/start-analysis`,
        method: "post",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json, */*"
        }
      })
      .then(
        response => {
            this.cameras = response.data
            this.overlay = false
          this.onAlert('success')
        }
      )
      .catch(
        () => {
          this.overlay = false
          this.onAlert('error')
        }
      )
    },
    onAlert: function(status) {
        this.status = status
        this.alert=true;
          setTimeout(()=>{
            this.alert=false
          },4000)
    }
  },
  created(){
    
  }
  
};
</script>