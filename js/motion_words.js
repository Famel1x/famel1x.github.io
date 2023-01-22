let stars  = document.getElementById('stars')
let moon = document.getElementById('moon')
let front = document.getElementById('front')
let text = document.getElementById('text')
let btn = document.getElementById('btn')

window.addEventListener('scroll', function(){
    let value = this.window.scrollY;
    stars.style.left =  value + 'px';
})