let ModeSombre = false;

function ChangeModeSombre(){
    if (ModeSombre){
        //Mode clair
        ModeSombre = false;
        document.documentElement.style.setProperty("--text-color","black")
        document.documentElement.style.setProperty("--background-color","#efe7e5")
        document.querySelector("#mode-clair-sombre").innerHTML ="Mode Sombre";   
    }
    else{
        //Mode sombre
        ModeSombre = true;
        document.documentElement.style.setProperty("--text-color","white")
        document.documentElement.style.setProperty("--background-color","black")
        document.querySelector("#mode-clair-sombre").innerHTML ="Mode Clair";
    }
}



document.addEventListener('DOMContentLoaded', function() {
    const btnCopy = document.querySelector('.btn-copy');
    const txt = "P-MC6GV6J9";

    btnCopy.addEventListener('click', () => {
        navigator.clipboard.writeText(txt);
    });
});