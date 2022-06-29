var password=document.getElementById("password1");

 function genPassword() {
    var chars = "123456789abcdefghijklmnpqrstuvwxyz!@#$%&*()[]{}/+_-ABCDEFGHIJKLMNPQRSTUVWXYZ";
    var passwordLength = 24;
    var password = "";
 for (var i = 0; i <= passwordLength; i++) {
   var randomNumber = Math.floor(Math.random() * chars.length);
   password += chars.substring(randomNumber, randomNumber +1);
  }
        document.getElementById("password1").value = password;
 }

