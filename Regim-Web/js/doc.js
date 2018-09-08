/* Loop through all dropdown buttons to toggle between hiding and showing its dropdown content
 This allows the user to have multiple dropdowns without any conflict */
var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}

const disp_a = document.getElementById("disp_a");
const restr_a = document.getElementById("restr_a");
const ite_a = document.getElementById("ite_a");
const met_a = document.getElementById("met_a");
const max_a = document.getElementById("max_a");

const disp = document.getElementById("disp");
const restr = document.getElementById("restrict");
const ite = document.getElementById("iter");
const met = document.getElementById("met");
const max = document.getElementById("max");
const doc = document.getElementById("documentation");

disp_a.addEventListener("click", ()=>{
  disp.style.display = "block";
  restr.style.display = "none";
  ite.style.display = "none";
  met.style.display = "none";
  max.style.display = "none";
  doc.style.display = "none";
})

restr_a.addEventListener("click", ()=>{
  disp.style.display = "none";
  restr.style.display = "block";
  ite.style.display = "none";
  met.style.display = "none";
  max.style.display = "none";
  doc.style.display = "none";
})

ite_a.addEventListener("click", ()=>{
  disp.style.display = "none";
  restr.style.display = "none";
  ite.style.display = "block";
  met.style.display = "none";
  max.style.display = "none";
  doc.style.display = "none";
})

met_a.addEventListener("click", ()=>{
  disp.style.display = "none";
  restr.style.display = "none";
  ite.style.display = "none";
  met.style.display = "block";
  max.style.display = "none";
  doc.style.display = "none";
})

max_a.addEventListener("click", ()=>{
  disp.style.display = "none";
  restr.style.display = "none";
  ite.style.display = "none";
  met.style.display = "none";
  max.style.display = "block";
  doc.style.display = "none";
})