let ModeSombre = false;

function ChangeModeSombre(){
    if (ModeSombre){
        //Mode clair
        ModeSombre = false;
        document.documentElement.style.setProperty("--text-color","black")
        document.documentElement.style.setProperty("--background-color","#efe7e5")
        document.querySelector("#mode-clair-sombre").innerHTML ="Mode Sombre";  
        document.querySelector(".icon-github").style.filter = "invert(0%)";
        document.querySelector(".icon-share").style.filter = "invert(0%)";
        document.querySelector(".icon-github-footer").style.filter = "invert(100%)";
    }
    else{
        //Mode sombre
        ModeSombre = true;
        document.documentElement.style.setProperty("--text-color","white")
        document.documentElement.style.setProperty("--background-color","black")
        document.querySelector("#mode-clair-sombre").innerHTML ="Mode Clair";
        document.querySelector(".icon-github").style.filter = "invert(100%)";
        document.querySelector(".icon-share").style.filter = "invert(100%)";
        document.querySelector(".icon-github-footer").style.filter = "invert(0%)";
    }
}



document.addEventListener('DOMContentLoaded', function() {
    const btnCopy = document.querySelector('.btn-copy');
    const txt = "P-MC6GV6J9";

    btnCopy.addEventListener('click', () => {
        navigator.clipboard.writeText(txt);
    });
});
