// const check = () =>{

function room(max,min){
    const roomNumber = Math.floor(Math.random() * (5 - 1 + 1)) + 1;
    return document.getElementById('room').innerHTML = roomNumber ;
}