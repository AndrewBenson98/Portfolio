// Run when the page loads
window.addEventListener("DOMContentLoaded", function () {
    mouseEvents();
});

function mouseEvents(){

const projectItems = document.querySelectorAll('.project-item-wrapper')

projectItems.forEach(function(project){

    project.addEventListener('mouseover', function(){
        project.childNodes[1].classList.add("img-darken")
    })

    project.addEventListener('mouseout', function(){
        project.childNodes[1].classList.remove("img-darken")
    })

})


}