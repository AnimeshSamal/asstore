<div class="collapse navbar-collapse" id="basicExampleNav13">

    <form class="navbar-search pl-0 ml-auto mt-3 mb-2 mt-md-0 mb-md-0 mr-3" action="">
      <div class="input-group d-block d-md-flex mb-0">
        <div class="input-group-prepend">
          <a href="#!" class="input-icon d-flex align-items-center" type="button"><i
              class="fas fa-search text-white mx-3"></i></a>
          <input class="form-control white-text rgba-black-light border-0 z-depth-0 pl-5" type="text"
            placeholder="Search" aria-label="Search">
        </div>
      </div>
    </form>

    <!-- Breadcrumbs -->
  <ol class="breadcrumb d-none d-xl-flex">
    <li class="breadcrumb-item"><a class="waves-effect" href="#!">Home</a></li>
    <li class="breadcrumb-item"><a class="waves-effect" href="#!">Templates</a></li>
    <li class="breadcrumb-item active">E-commerce</li>
  </ol>
  <!-- Breadcrumbs -->


  <!-- Collapse button -->
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#basicExampleNav13"
    aria-controls="basicExampleNav13" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

 
  <!-- Links -
  <nav class="navbar navbar-expand-lg navbar-light bg-light container-fluid d-inline-flex  bd-highlight row">



  from django.db import models

class Customer(models.Model):
    first_name = models.CharFeild(max_length=50)
    last_name = models.CharFeild(max_lenght=50)
    email = models.EmailFeild(max_length=20)
    phone = models.CharFeild(max_lenght=10)
    password = models.CharFeild(max_lenght=10)
    address = models.CharFeild(max_lenght=200)
    city = models.CharFeild(max_lenght=100)
    state = models.CharFeild(max_lenght=100)
    pin =  models.CharFeild(max_lenght=10)