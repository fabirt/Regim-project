function w3_bar_menu() {
    const bars = "fa fa-bars";
    const times = "fa fa-times";
    const menuIcon = document.getElementById("menu-icon");
    const iconClassName = menuIcon.className;
    if (iconClassName==bars){
        document.getElementById("mySidebar").style.animation = "animateleft 0.4s"
        document.getElementById("mySidebar").style.width = "60%";
        document.getElementById("mySidebar").style.display = "block";
        document.getElementById("myOverlay").style.display = "block";
        document.getElementById("menu-icon").className = times;
    }else{
        document.getElementById("mySidebar").style.animation = "animaterightt 0.4s"
        document.getElementById("mySidebar").style.display = "block";
        setTimeout(()=>{
            document.getElementById("mySidebar").style.display = "none";
        },300)
        document.getElementById("myOverlay").style.display = "none";
        document.getElementById("menu-icon").className = bars;
        
    }
}

let pressed = false;
function nocMode(){
    const nocElements = document.getElementsByClassName("noc");
    for(let i = 0; i< nocElements.length; i++){
        if(pressed == false){
            nocElements[i].style.backgroundColor = "#32393f";
            nocElements[i].style.color = "white";
        }else{
            nocElements[i].style.backgroundColor = "#fff";
            nocElements[i].style.color = "black";
        } 
    }
    pressed = !pressed;
}
