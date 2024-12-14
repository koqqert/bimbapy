'use strict';
//задание 10
switch (browser) {
  case 'Edge':
    alert( "You've got the Edge!" );
    break;

  case 'Chrome':
  case 'Firefox':
  case 'Safari':
  case 'Opera':
    alert( 'Okay we support these browsers too' );
    break;

  default:
    alert( 'We hope that this page looks ok!' );
}

if (browser == 'Edge'){
  alert( "You've got the Edge!" );
} else if (browser == 'Chrome'
  || browser == 'Firefox'
  || browser == 'Safari'
  || browser == 'Opera') {
  alert( 'Okay we support these browsers too' );
} else {
  alert( 'We hope that this page looks ok!' );
}

//задание 11
const number = +prompt('Введите число между 0 и 3', '')

switch (number) {
  case 0: 
    alert('Вы ввели число 0');
    break;

  case 1:
    alert('Вы ввели число 1');
    break;

  case 2:
  case 3:
    alert('Вы ввели число 2, а может и 3');
}

//задание 12
function checkAge(age) {
  return (age > 18) || confirm('Родители разрешили?');
 }

function checkAge2(age) {
  return (age > 18) ? true : confirm('Родители разрешили?');
}

//проходил блок качество кода
//задание 15
let user = {};
user.name = 'John';
user.surname = 'Smith';
user.name = 'Pete';
delete user.name;

//задание 16
let schedule = {};

alert( isEmpty(schedule) ); // true

schedule["8:30"] = "get up";

alert( isEmpty(schedule) ); // false

function isEmpty(obj) {
  for(let key in obj) {
    return false;
  }
  return true;
}

//задание 17
let ssalaries = {
  John: 100,
  Ann: 160,
  Pete: 130
}
let sum = 0;

for (let salary in ssalaries){
  sum += ssalaries[salary];
}

alert(sum);
//задание 18
let menu = {
  width: 200,
  height: 300,
  title: "My menu"
};

function multiplyNumeric(obj) {
  for (let key in obj){
    if (typeof obj[key] === 'number'){
      obj[key] *= 2;
    }
  }
}

//задание 19
let calculator = {
  sum() {
    return this.a + this.b;
  },
  mul() {
    return this.a * this.b;
  },
  read() {
    this.a = +prompt('Enter first number', 0);
    this.b = +prompt('Enter second number', 0);
  }
}

//задание 20
function Calculator(){
  this.read = function() {
    this.a = +prompt('Enter first number', 0);
    this.b = +prompt('Enter second number', 0);
  }
  this.sum = function() {
    return this.a + this.b;
  }
  this.mul = function() {
    return this.a * this.b;
  }
}

//задание 21
function Accumulator(startingValue){
  this.value = startingValue;
  this.read = function() {
    this.value += +prompt('Enter a number', 0);
  }
}

//задание 22
function readNumber(){
  let number;

  do {
    num = prompt('Enter a number', 0)
  } while (!isFinite(num));
  if (num === null || num === "") return null;
  return +num;
}

//задание 23
function cheackSpam(str){
  let lowerStr = str.toLowerCase();
  
  return lowerStr.includes('viagra') || lowerStr.includes('xxx');
}

//задание 24
function truncate(str, maxlength){
  return (str.lenght > maxlength) ?
    str.slice(0, maxlength - 1) + '...' : str; //один спец. символ
}
//задание 25
function extractCurrencyValue(str){
  return +str.slice(1);
}

//задание 26
let styles = ['Джаз', 'Блюз'];
styles.push('Рок-н-ролл');
styles[Math.floor((styles.lenght -1) / 2)] = 'Классика';
alert(styles.shift());
styles.unshift('Рэп','Регги');

//задание 27
function sumInput(){
  let numbers = [];

  while(true){

    let value = prompt('enter a number: ', 0)

    if (value === '' || value === null || !isFinite(value)) break;

    numbers.push(+value);
  }

  let sum = 0;
  for (let number of numbers) {
    sum += number;
  }
  return numbers
}

//задание 28
function camelize(str){
  return str.split('-').map((word, index) =>
    index == 0? word : word[0].toUpperCase() + word.slice(1)
  ).join('');
}
//задание 29
function filterRange(arr, a, b){
  return arr.filter(value => (value <= a && value <= b));
}
//задание 30
function filterRangeInPlace(arr, a, b) {

  for (let i = 0; i < arr.length; i++) {
    let val = arr[i];

    if (val < a || val > b) {
      arr.splice(i, 1);
      i--;
    }
  }

}
//задание 31 
let arr2 = [5, 2, 1, -10, 8];
arr2.sort((a, b) => b - a);
alert( arr2 );

//задание 32
function Calculator(){

  this.methods = {
    '+': (a, b) => a + b,
    '-': (a, b) => a - b,
  };

  this.calculate = function(str){
    let arr = str.split(' '),
      a = +arr[0],
      op = arr[1],
      b = +arr[2]

    if (!this.methods[op] || isNaN(a) || isNaN(b)) {
      return NaN;
    }

    return this.methods[op](a, b);
  }

  this.addMethod = function(name, func){
    this.methods[name] = func;
  };

}
//задание 33
let Vasya = { name: "Вася", age: 25 };
let Petya = { name: "Петя", age: 30 };
let Masha = { name: "Маша", age: 28 };

let uusers = [ Vasya, Petya, Masha ];

let names = uusers.map(item => item.name);

//задание 34
let vasya = { name: "Вася", surname: "Пупкин", id: 1 };
let petya = { name: "Петя", surname: "Иванов", id: 2 };
let masha = { name: "Маша", surname: "Петрова", id: 3 };

let users = [ vasya, petya, masha ];

let usersMapped = users.map(user => ({
  fullName : `${user.name} ${user.surname}`,
  id : user.id,
}))
//задание 35 (те же имена)
function sortByAge(users){
  users.sort((a, b) => a.age - b.age);
}

//задание 36
function unique(arr) {
  return Array.from(new Set(arr))
}

let values = ["Hare", "Krishna", "Hare", "Krishna",
  "Krishna", "Krishna", "Hare", "Hare", ":-O"
];

//задание 37
let arre = ["nap", "teachers", "cheaters", "PAN", "ear", "era", "hectares"];

function aclean(arre){
  let map = new Map();

  for (let word of arre){
    let sorted = word.toLowerCase().split('').sort().join('');
    map.set(sorted, word);
  }

  return Array.from(map.values());

};

//задание 38
let salaries = {
  "John": 100,
  "Pete": 300,
  "Mary": 250
};

function topSalary(salaries){

  let max = 0;
  let maxName = 0;

  for(const[name, salary] of Object.entries(salaries)){
    if (max < salary){
      max = salary;
      maxName = name;
    }
  }

  return maxName;
  
};

//задание 39
let d = new Date(2012,1,2,3,12);
alert(d)
//задание 40
function getWeekDay(date){
  let days = ['ВС', 'ПН', 'ВТ', 'СР', 'ЧТ', 'ПТ', 'СБ'];

  return days[date.getDay()]

}

//задание 41
function getSecondsToday(){
  let now = new Date();

  let today = new Date(now.getFullYear(), now.getMonth(), now.getDate());

  let diff = now - today;
  return Math.floor(diff / 1000);
}
//задание 42
function getSecondsToTomorrow(){
  let now = new Date();
  let tomorrow = new Date(now.getFullYear(), now.getMonth(), now.getDate() + 1);
  
  let diff = tomorrow - now;
  return Math.round(diff / 1000);
}

//задание 43
let user = {
  name: "Василий Иванович",
  age: 35
};
user2 = JSON.parse(JSON.stringify(user))

//задание 44
let room = {
  number: 23
};

let meetup = {
  title: "Совещание",
  occupiedBy: [{name: "Иванов"}, {name: "Петров"}],
  place: room
};

// цикличные ссылки
room.occupiedBy = meetup;
meetup.self = meetup;

alert( JSON.stringify(meetup, function replacer(key, value) {
  return (key != '' && value == meetup) ? undefined : value;
}));
//задание 45
function sumTo(n){
  let sum = 0;
  for (let i = 1; i <= n; i++){
    sum += i;
  }
  return sum;
}
function sumTo(n){
  if (n == 1) return 1;
  return n + sumTo(n - 1);
}

//задание 46
function factorial(n){
  return (n != 1) ? n * factorial(n - 1) : 1;
}

//задание 47
function sum(a){
  return function(b){
    return a + b;
  }
}

//задание 48
let arr = [1, 2, 3, 4, 5, 6, 7];

function inBetween(a,b){
  return function(x){
    return x >= a && x <= b;
  };
}

function inArray(arr){
  return function(x){
    return arr.includes(x);
  };
}
//практика на codewars
function humanReadable (seconds) {
  const hours = Math.floor(seconds / 3600).toString.padStart(2,'0');
  const minutes = Math.floor((seconds % 3600) / 60).toString().padStart(2,'0');
  const secs = Math.floor(seconds % 60).toString.padStart(2,'0');

  return `${hours}:${minutes}:${secs}`;
}

function moveZeros(arr) {
  let nonZeros = [];
  let zeroCount = 0;
  
  for (let element of arr){
    if (element === 0){
        zeroCount++;
    } else {
        nonZeros.push(element);
    }
  }
  
  while (zeroCount > 0){
      nonZeros.push(0);
      zeroCount--;
  }
  
  return nonZeros;
}

function toCamelCase(str) {
  let words = str.split(' ');
  let result = '';

  for (let i = 0; i < words.length; i++) {
    let word = words[i];
    result += word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
  }

  return result;

}

class Clock {
  constructor({template}){
    this.template = template;
  }

  render(){
    let date = new Date();

    let hours = date.getHours();
      if (hours < 10) hours = '0' + hours;
  
    let mins = date.getMinutes();
      if (mins < 10) mins = '0' + mins;
  
    let secs = date.getSeconds();
      if (secs < 10) secs = '0' + secs;
    
    let output = template
        .replace('h', hours)
        .replace('m', mins)
        .replace('s', secs);
  
    console.log(output);
    }
  
  stop() {
    clearInterval(this.timer);
  }

  start() {
    this.render();
    this.timer = setInterval(() => this.render(), 1000);
  }
}

class ExtendedClock extends Clock {
  constructor(options) {
    super(options);
    let {precessions = 1000} = options;
    this.precision = precisions;
  }

  start() {
    this.render();
    this.timer = setInterval(() => this.render(), this.precision);
  }
}


function parseInt(words) {
  let result = 0;
  let current = 0;
  let parts = words.split(/[\s-]+/);

  for (let part of parts) {
      let value = numberWords[part];
      if (value >= 1000) {
          current *= value;
          result += current;
          current = 0;
      } else if (value >= 100) {
          current *= value;
      } else {
          current += value;
      }
  }

  return result + current;
}

function high(x) {
  function wordScore(word){
    return word.split('').reduce((score, char) => score + (char.charCodeAt(0) - 96), 0);
  }
  
  const words = x.split(' ');

  let maxScore = 0;
  let maxWord = '';

  for (let word of words) {
    const score = wordScore(word);
    if (score > maxScore) {
        maxScore = score;
        maxWord = word;
    }
  }

  return maxWord;
}

function domainName(url){
  url = url.replace('https://', '').replace('http://', '').replace('www.', '');

  const parts = url.split('/');
  const domainParts = parts[0].split('.');

  return domainParts[0];
  
}

class FormatError extends SyntaxError {
  constructor(message){
    super(message);
     this.name = 'formatError';
  }
}

function delay(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}



class HttpError extends Error {
  constructor(response) {
    super(`${response.status} for ${response.url}`);
    this.name = 'HttpError';
    this.response = response;
  }
}

async function loadJson(url) {
  let response = await fetch(url)
    if (response.status == 200) {
      let json = await response.json();
      return json;
    }
    throw new HttpError(response);
}

// Запрашивать логин, пока github не вернёт существующего пользователя.
async function demoGithubUser() {
  
  let user;
  while(true){
    let name = prompt("Введите логин?", "iliakan");

    try {
      user = await loadJson(`https://api.github.com/users/${name}`);
      break;
    } catch(err) {
      if (err instanceof HttpError && err.response.status == 404) {
        alert("Такого пользователя не существует, пожалуйста, повторите ввод.");
      } else {
        throw err;
      }
    }
  }

  alert(`Полное имя: ${user.name}.`);
  return user;
}

demoGithubUser();

let table = document.body.firstElementChild;

    for (let i = 0; i < table.rows.length; i++) {
      let row = table.rows[i];
      row.cells[i].style.backgroundColor = 'red';
    }

let ul = document.createElement('ul');
document.body.append(ul);

while (true) {
  let data = prompt("Введите текст для элемента списка", "");

  if (!data) {
    break;
  }

  let li = document.createElement('li');
  li.textContent = data;
  ul.append(li);
}

function createTree(container, obj) {
  container.append(createTreeDom(obj));
}

function createTreeDom(obj) {
  let ul = document.createElement('ul');
  
  for (let key in obj) {
    let li = document.createElement('li');
    li.innerHTML(key);

    let childrenUL = createTreeDom(obj[key]);
    if (childrenUL) {
      li.append(childrenUL);
    }
    ul.append(li);
  }

  return ul;
}

function update() {
  let clock = document.getElementById('clock');
  let date = new Date();
  let hours = date.getHours();
  if (hours < 10) hours = "0" + hours;
  clock.children[0].innerHTML = hours;

  let minutes = date.getMinutes();
  if (minutes < 10) minutes = "0" + minutes;
  clock.children[1].innerHTML = minutes;

  let seconds = date.getSeconds();
  if (seconds < 10) seconds = '0' + seconds;
  clock.children[2].innerHTML = seconds;
}

let timerId;

function start() {
  timerId = setInterval(update, 1000);
  update();
}

function stop() {
  clearInterval(timerId);
  timerId = null;
}

let fieldonclick = function(event){ //field.onclick

  let fieldCoords = this.getBoundingClientRect();
  
  let ballCoords = {
    top: event.clientY - fieldCoords.top - field.clientTop - ball.clientHeight/2,
    left: event.clientX - fieldCoords.left - field.clientLeft - ball.clientWidth/2
  }

  if (ballCoords.top < 0) ballCoords.top = 0;
  if (ballCoords.left < 0) ballCoords.left = 0;

  if (ballCoords.left + ball.clientWidth > field.clientWidth) {
    ballCoords.left = field.clientWidth - ball.clientWidth;
  }

  if (ballCoords.top + ball.clientHeight > field.clientHeight) {
    ballCoords.top = field.clientHeight - ball.clientHeight;
  }

  ball.style.top = ballCoords.top + 'px';
  ball.style.left = ballCoords.left + 'px';
}

function hexStringToRGB(hexString) {
  let strColor = hexString.toLowerCase().replace("#", ' ');
  
  let r = parseInt(strColor.substring(0,2), 16);
  let g = parseInt(strColor.substring(2,4), 16);
  let b = parseInt(strColor.substring(4,6), 16);

  return {r: r, g: g, b: b};
}

let tooltip;

document.onmouseover = function(event){
  let anchorElem = event.target.closest('[data-tooltip]');

  if (!anchorElem) return;

  tooltip = showTooltip(anchorElem, anchorElem.dataset.tooltip);
}

document.onmouseout = function(event){
  if (tooltip) {
    tooltip.remove();
    tooltip = null;
  }
}

function showTooltip(anchorElem, html) {
  let tooltipElem = document.createElement('div');
  tooltipElem.className = 'tooltip';
  tooltipElem.innerHTML = html;
  document.body.append(tooltipElem);

  let coords = getBoundingClientRect();
  let left = coords.left + (anchorElem.offsetWidth - tooltipElem.offsetWidth) / 2;
  if (left < 0) left = 0;

  let top = coords.top - tooltipElem.offsetHeight - 5;

  if (top < 0) {
    top = coords.top + anchorElem.offsetHeight + 5;
  }
  tooltipElem.style.left = left + 'px';
  tooltipElem.style.top = top + 'px';

  return tooltipElem;
}

let thumb = slider.querySelector('.thumb');

thumb.onmousedown = function(event) {
  event.preventDefault();

  let shiftX = event.clientX - thumb.getBoundingClientRect().left;

  document.addEventListener('mousemove', onMouseMove);
  document.addEventListener('mouseup', onMouseUp);
  
  function omMouseMove(event){ 
    let newLeft = event.clientX - shiftX - slider.getBoundingClientRect().left;

    if (newLeft < 0) {
      newLeft = 0;
    }

    let rightEdge = slider.offsetWidth - thumb.offsetWidth;
    if (newLeft > rightEdge) {
      newLeft = rightEdge;
    }

    thumb.style.left = newLeft + 'px';
    }

  function onMouseUp(event) {
    document.removeEventListener('mouseup', onMouseUp);
    document.removeEventListener('mousemove', onMouseMove);
  }
}

thumb.ondragstart = function() {
  return false;
};


function runOkeys(func, ...codes) {
  let pressed = new Set();

  document.addEventListener('keydown', function(event) {
    pressed.add(event.code); 
  
    for (let code of codes) {
      if (!pressed.has(code)) {
        return;
      }
    }

    pressed.clear();
    func();
  });
  
  document.addEventListener('keyup', function(event) {
    pressed.delete(event.code);
  });
}