const PAYDAY_WEEKDAY = 4; // 0=Sun, 4=Thu

/**
 * Calculates the date of the next payday based on the current date and payday weekday.
 * 
 */
function getNextPayday(date, paydayWeekday = PAYDAY_WEEKDAY) {
  const dayIndex = date.getDay();
  let diff = paydayWeekday - dayIndex;

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

let tempButton = document.getElementById("calculate-btn");
tempButton.addEventListener("click", function() {
  let tempCalc = document.getElementById("temp-input");
  let spending = tempCalc.value - 376.10;
  tempCalc.value = `${spending.toFixed(2)}`;
});