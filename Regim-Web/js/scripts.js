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
        setTimeout(function(){
            document.getElementById("mySidebar").style.display = "none";
        },300)
        document.getElementById("myOverlay").style.display = "none";
        document.getElementById("menu-icon").className = bars;
        
    }
    
    
}
