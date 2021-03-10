btn = document.getElementById("btn");
btn.addEventListener("click", (e) =>{
    console.log("Hola")
    var http = new XMLHttpRequest();
    var url = "http://localhost:5000/send";
    let Datos = {
        art: document.getElementById("txt_nombre").value, 
        precio: document.getElementById("txt_precio").value,
        color: document.getElementById("txt_color").value
    };
    document.getElementById("txt_nombre").value = "";
    document.getElementById("txt_precio").value = "";
    document.getElementById("txt_color").value = "";

    http.open("POST", url, true);
    http.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    http.onreadystatechange = function() {
        if(http.readyState == 4 && http.status == 200) { 
        //Si se ha concluido el proceso y el estatus del servidor es ok enviamos la informacion al DOM
        document.getElementById("respuesta").innerHTML = http.responseText;
        console.log(http.responseText);

        }
    }
    http.send(JSON.stringify(Datos));
});