
<template>
<div id="app">

<v-content>

    <v-container fill-height fluid>
  <v-row align="center"
      justify="center">
      <v-col cols="12" sm="12" md="10" lg="10">
          
         <v-data-table
            :headers="headers"
            :items="cameras"
            :items-per-page="20"
            class="elevation-1"
          ></v-data-table>
    </v-col>
  </v-row>
</v-container>
     
    </v-content>
</div>
</template>


<script>
import BACKEND_URL from '../urls';
import axios from 'axios';

export default {
  name: "ConfigPage",
  props: ["cameras"],
  data: () => ({
    headers: [
          {
            text: 'Имя камеры',
            align: 'start',
            sortable: false,
            value: 'title',
          },
          { text: 'URL для RGB скриншотов', value: 'screen_url' },
          { text: 'URL для облака точек', value: 'tof_url' },

        ],
    cameras: [],
  }),
  methods: {
  },
  mounted() {
    axios.get(`${BACKEND_URL}/v0/cameras/get-all-cameras`)
    .then(response => {
      this.cameras = response.data;

      })
  },
  created(){
    
  }
  
};
</script>