//   for validating the name
  function namevalidate() {
    var name = document.getElementById("name").value;
    var regName = /\d+$/g;
    if (
      name == "" ||
      (name.length < 3 && name.length < 25) ||
      regName.test(name)
    ) {
      document.getElementById("nameerror").innerHTML =
        "Please enter a valid name";
      
    } else {
      document.getElementById("nameerror").innerHTML = "";
      
    }
  }

//   for validating the email
  function emailvalidate() {
    var email = document.getElementById("email").value;
    var regEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/g;
    if (email == "" || !regEmail.test(email)) {
      document.getElementById("emailerror").innerHTML =
        "Please enter a valid email";
    } else {
      document.getElementById("emailerror").innerHTML = "";
    
    }
  }
  function emailcheck() {
    var email = document.getElementById("email").value;
    var regEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/g;
    if (regEmail.test(email)) {
      document.getElementById("emailerror").innerHTML = "";
    }
  }

//   for validating the subject
  function subjectvalidate() {
    var sub = document.getElementById("subject").value;
    if (sub == "") {
      document.getElementById("subjecterror").innerHTML ="Please enter the subject";
    }
    else{
        document.getElementById("subjecterror").innerHTML ="";
    }
  }

// for validating the message
  function messagevalidate() {
    var msg = document.getElementById("message").value;
    if (msg == "") {
      document.getElementById("messageerror").innerHTML ="Please enter the message";
    }
    else{
        document.getElementById("messageerror").innerHTML ="";
    }
  }

const hamburger = document.querySelector(".hamburger");
const navMenu = document.querySelector(".nav-menu"); 
  
hamburger.addEventListener("click",() => {
      hamburger.classList.toggle("active");
      navMenu.classList.toggle("active");
  })
