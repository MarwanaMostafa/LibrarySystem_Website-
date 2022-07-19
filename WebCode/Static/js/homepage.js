
function whenclick(){
 var email  =document.getElementById("em").value;
 var password = document.getElementById("pas").value;
 var usernmae = document.getElementById("use").value;
var type = document.getElementById("type").value;

var valid=true;
var count =password.length;
    for(var i=0;i<count;i++){
        if (count<7||password[i]=="#"||password[i]=="$"||password[i]=="&"||password[i]=="*"){
            valid=false;
           alert("invalid password\n the password should be more than 7 aphapet characters");
    }
/*
if (valid){
    
    //send data to the backend
    //recive request shoow if the data is already exist or not
    //then makes alert depends on the recieved data
}*/

    
}
}

var submittbutton= document.getElementById("sub");
submittbutton.onclick=whenclick;




function whenlogin(){
    var usernmae= document.getElementById("unamid");
    var password =document.getElementById("pasid");
   

     
var valid=true;
var count =password.length;
    for(var i=0;i<count;i++){
        if (count<7||password[i]=="#"||password[i]=="$"||password[i]=="&"||password[i]=="*"){
            valid=false;
           alert("invalid password\n the password should be more than 7 aphapet characters");
    }
/*
if (valid){
    
    //send data to the backend
    //recive request shoow if the data is already exist or not
    //then makes alert depends on the recieved data
}*/

}

}

var login =document.getElementById("subid");
  login.onclick=whenlogin;