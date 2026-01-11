// js-to-python-exercises.js
// Day 1 Translation Exercises: JavaScript → Python
// For each function below, write the equivalent Python version!

// === Level 1 – Super Basics ===

// 1.
function greet(name) {
  return "Hello, " + name + "!";
}

// 2.
function isPositive(num) {
  return num > 0;
}

// 3.
function double(number) {
  return number * 2;
}

// 4.
function getLength(str) {
  return str.length;
}

// 5.
function sayYesOrNo(isCool) {
  if (isCool) {
    return "Yes!";
  } else {
    return "No :(";
  }
}

// 6.
function add(a, b) {
  return a + b;
}

// 7.
function isAdult(age) {
  return age >= 18;
}

// 8.
function shout(text) {
  return text.toUpperCase();
}

// === Level 2 – Conditionals + Simple Logic ===

// 9.
function getGrade(score) {
  if (score >= 90) return "A";
  if (score >= 80) return "B";
  if (score >= 70) return "C";
  if (score >= 60) return "D";
  return "F";
}

// 10.
function isEven(num) {
  return num % 2 === 0;
}

// 11.
function max(a, b) {
  if (a > b) return a;
  return b;
}

// 12.
function describeTemperature(temp) {
  if (temp >= 30) return "Hot";
  if (temp >= 20) return "Warm";
  if (temp >= 10) return "Cool";
  return "Cold";
}

// 13.
function canVote(age, isCitizen) {
  return age >= 18 && isCitizen === true;
}

// 14.
function getMessage(hour) {
  if (hour < 12) return "Good morning!";
  if (hour < 17) return "Good afternoon!";
  return "Good evening!";
}

// === Level 3 – Simple Loops & Lists ===

// 15. (Note: In JS we usually console.log, in Python you'll use print)
function countTo(n) {
  for (let i = 1; i <= n; i++) {
    console.log(i);
  }
}

// 16.
function sumNumbers(n) {
  let sum = 0;
  for (let i = 1; i <= n; i++) {
    sum += i;
  }
  return sum;
}

// 17.
function getFirst(arr) {
  return arr[0];
}

// 18.
function getLast(arr) {
  return arr[arr.length - 1];
}

// 19. (Note: In Python this becomes a for loop with print)
function printEach(names) {
  for (let name of names) {
    console.log(name);
  }
}

// 20.
function countItems(arr) {
  return arr.length;
}

// === Optional Bonus Stretch (if you finish early) ===
function isPalindrome(word) {
  const cleaned = word.toLowerCase();
  return cleaned === cleaned.split('').reverse().join('');
}

// You can test any of these in the console like:
//console.log(greet("Alex"));          // "Hello, Alex!"
// console.log(getGrade(85));           // "B"
// console.log(sumNumbers(5));          // 15
// console.log(getLast([10, 20, 30]));  // 30