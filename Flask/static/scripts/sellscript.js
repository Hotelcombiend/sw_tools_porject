var y = 0
var p = 0
var three = 0
var four = 0
var five = 0
document.getElementById('price').innerHTML = y;
document.getElementById('price2').innerHTML = p;
document.getElementById('price3').innerHTML = three;
document.getElementById('price4').innerHTML = four;
document.getElementById('price5').innerHTML = five;
// var x = document.getElementsByClassName('btnmiplus')
// r = Array.from(x)
// console.log(x)
// console.log(r)

// var t = ['h', 'k', 't']
// console.log(t)
// r.forEach(element => {
//     console.log(element.type)
// });
function btnminus_1() {
    var x = document.getElementById('btnminus')
    if (x.className === "minus" && y > 0) {
      y -= 1;
      document.getElementById('price').innerHTML = y;
    }
  }

  function btnplus_1() {
    var x = document.getElementById('btnplus')
    if (x.className === "plus") {
      y += 1;
      document.getElementById('price').innerHTML = y;
    } 
  }

///2///
  function btnminus1() {
    var x = document.getElementById('btnminus2')
    if (x.className === "minus" && p > 0) {
      p -= 1;
      document.getElementById('price2').innerHTML = p;
    }
  }

  function btnplus1() {
    var x = document.getElementById('btnplus2')
    if (x.className === "plus") {
      p += 1;
      document.getElementById('price2').innerHTML = p;
    } 
  }

///3///
function btnminus_2() {
  var x = document.getElementById('btnminus3')
  if (x.className === "minus" && three > 0) {
    three -= 1;
    document.getElementById('price3').innerHTML = three;
  }
}

function btnplus_2() {
  var x = document.getElementById('btnplus3')
  if (x.className === "plus") {
    three += 1;
    document.getElementById('price3').innerHTML = three;
  } 
}

///4///
function btnminus_3() {
  var x = document.getElementById('btnminus4')
  if (x.className === "minus" && four > 0) {
    four -= 1;
    document.getElementById('price4').innerHTML = four;
  }
}

function btnplus_3() {
  var x = document.getElementById('btnplus4')
  if (x.className === "plus") {
    four += 1;
    document.getElementById('price4').innerHTML = four;
  } 
}

///5///
function btnminus_4() {
  var x = document.getElementById('btnminus5')
  if (x.className === "minus" && five > 0) {
    five -= 1;
    document.getElementById('price5').innerHTML = five;
  }
}

function btnplus_4() {
  var x = document.getElementById('btnplus5')
  if (x.className === "plus") {
    five += 1;
    document.getElementById('price5').innerHTML = five;
  } 
}



console.log(y)