const PAYDAY_WEEKDAY = 4; // 0=Sun, 4=Thu
let paycheck = 0; // This amount will be adjusted for user input.
let bills_weekly = 376.10; // This amount is mine, however this will be adjusted for user input.

/**
 * Calculates the date of the next payday based on the current date and payday weekday.
 * 
 */
function getNextPayday(date, payday = PAYDAY_WEEKDAY) {
  const dayIndex = date.getDay();
  let diff = payday - dayIndex;

  if (diff < 0) diff += 7;

  const next = new Date(date);
  next.setDate(date.getDate() + diff);
  return next;
}

/** 
 * Creates a pay period object with start and end dates based on the given payday date.
*/
function createPayPeriod(paydayDate) {
  const start = new Date(paydayDate);
  const end = new Date(paydayDate);
  end.setDate(end.getDate() + 6);

  return { start, end };
}

/**
 * Calculates the current pay period based on today's date and the defined payday weekday.
 */
function getCurrentPayPeriod() {
  const today = new Date();
  const nextPayday = getNextPayday(today);

  // If today *is* payday, the period starts today
  if (today.toDateString() === nextPayday.toDateString()) {
    return createPayPeriod(today);
  }

  // Otherwise, the current period started last Thursday
  const lastPayday = new Date(nextPayday);
  lastPayday.setDate(nextPayday.getDate() - 7);

  return createPayPeriod(lastPayday);
}

const period = getCurrentPayPeriod();
document.getElementById("pay-period").innerText =`Current Pay Period: ${period.start.toDateString()} → ${period.end.toDateString()}`;

let calcButton = document.getElementById("calculate-btn");
let awaiting_bills = false;
let restart = false;
calcButton.addEventListener("click", () => {

  const input =document.getElementById("calc-input");
  const label = document.getElementById("pay-label");
  if (!awaiting_bills && !restart) {
    //First press, get paycheck amount
    paycheck = parseFloat(input.value);
    awaiting_bills = true;
    label.innerText = "Enter Weekly Bills:";
    input.setAttribute("placeholder", "Enter your weekly bills");
    input.value = "";
    calcButton.innerText = "Calculate Spending";
  }
  else if (restart == true) {
    label.innerText = "Enter Pay Amount:";
    input.setAttribute("placeholder", "Enter your pay amount");
    calcButton.innerText = "Submit";
    input.value = "";
    restart = false;
  }
  else {
    input.value != "" ? bills_weekly = parseFloat(input.value) : bills_weekly = bills_weekly; // Keep the default if no input is provided
    let spending = paycheck - bills_weekly;
    label.innerText = "Your leftover spending money is:";
    input.value = `${spending.toFixed(2)}`;
    calcButton.innerText = "Restart";
    awaiting_bills = false;
    restart = true;
  }
});