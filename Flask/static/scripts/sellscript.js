var y = 0
document.getElementById('price').innerHTML = y;
// var x = document.getElementsByClassName('btnmiplus')
// r = Array.from(x)
// console.log(x)
// console.log(r)

// var t = ['h', 'k', 't']
// console.log(t)
// r.forEach(element => {
//     console.log(element.type)
// });
function myFunction() {
    var x = document.getElementById('btnminus')
    if (x.className === "minus" && y > 0) {
      y -= 1;
      document.getElementById('price').innerHTML = y;
    }
  }

  function btnplus1() {
    var x = document.getElementById('btnplus')
    if (x.className === "plus") {
      y += 1;
      document.getElementById('price').innerHTML = y;
    } 
  }

console.log(y)