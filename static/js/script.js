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
if(document.getElementById("pay-period")) {
  document.getElementById("pay-period").innerText =`Current Pay Period: ${period.start.toDateString()} → ${period.end.toDateString()}`;
}

let calcButton = document.getElementById("calculate-btn");
let awaiting_bills = false;
let restart = false;
if(calcButton){
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
      label.innerText = "Enter Weekly Pay Amount:";
      input.setAttribute("placeholder", "Enter your weekly pay amount");
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
}

/* End of Script that only pertains to the base page with the calculator */

const submitButton = document.getElementById("save-transaction-btn");
const transactionForm = document.getElementById("transaction-form");


/**
 * Initializes edit functionality for the provided edit buttons.
 *
 * For each button in the `editButtons` collection:
 * - Retrieves the associated transaction's ID upon click.
 * - Fetches the content of the corresponding transaction.
 * - Populates the transaction form with the chosen trnasaction's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{transactionId}` endpoint.
 */
document.querySelectorAll('.edit-btn').forEach(button => {
  button.addEventListener('click', function () {

    const row = this.closest('tr');
    document.getElementById('transaction-form').scrollIntoView({ behavior: 'smooth' });

    document.getElementById('transaction-id').value = row.dataset.id;

    document.getElementById('id_description').value = row.dataset.description;

    document.getElementById('id_amount').value = row.dataset.amount;

    document.getElementById('id_type').value = row.dataset.type;

    document.getElementById('id_date').value = row.dataset.date;

    document.getElementById('id_category').value = row.dataset.category;

    submitButton.innerText = "Update";
    
  });
});
/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated transaction's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific transaction.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

document.addEventListener('DOMContentLoaded', () => {

  const deleteButtons = document.getElementsByClassName("delete-btn");
  const deleteConfirm = document.getElementById("deleteConfirm");
  

  document.querySelectorAll('.delete-btn').forEach(button => {
    button.addEventListener('click', function () {
      const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
      const row = this.closest('tr');
      const transactionId = row.dataset.id;
      deleteConfirm.href = `delete_transaction/${transactionId}`;
      deleteModal.show();
    });
  });
});
