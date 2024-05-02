import axios from "axios";
import { createStore } from "vuex";

const state = {
  data: null,
  title: "",
};
const mutations = {
  setData(state, data) {
    state.data = data;
  },
  setTitle(state, title) {
    state.title = title;
  },
};

const actions = {
  fetchData({ commit }) {
    const currentUri = window.location.pathname;
    let title = "";
    let path = "";

    // Establecer el título y la ruta dependiendo de la URI actual
    if (currentUri === "/listLastSevenDays") {
      title = "Tabla de Tareas últimos siete días";
      path = "http://localhost:8000/api/v1.0/tasksLastSevenDays/";
    } else {
      title = "Tabla de Tareas";
      path = "http://localhost:8000/api/v1.0/tasks/";
    }

    return axios
      .get(path)
      .then((response) => {
        commit("setData", response.data);
        commit("setTitle", title);
      })
      .catch((error) => {
        console.error("Error al obtener datos:", error);
      });
  },
};
const getters = {};

const store = createStore({
  state,
  getters,
  actions,
  mutations,
});

export default store;
