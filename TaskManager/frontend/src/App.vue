<template>
  <div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary appHeader">
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="#">Home</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              List
            </a>
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">All</a></li>
              <li><a class="dropdown-item" href="#">Last seven days</a></li>
            </ul>
          </li>
        </ul>
      </div>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body{margin: 0;}
.appHeader{
background-color: #87a87a !important;
color: #DCDFD3
}

.appHeader .dropdown-menu{
  background-color: #87a87a !important;


}
.dropdown-item, .nav-link{
  color: #DCDFD3 !important;
  font-size: 15px;
}
</style>
