// document.addEventListener('DOMContentLoaded', () => {
//     document.querySelectorAll('input[name="task_ids"]').forEach(function (checkbox) {
//         checkbox.addEventListener('change', function () {
//             if (this.checked) {
//                 document.getElementById('complete_tasks_form').submit();
//             }
//         });
//     });
// });
// console.log('hello world');

// function markTaskComplete(checkbox) {
//     if (checkbox.checked) {
//         var form = document.getElementById('complete_tasks_form');
//         var formData = new FormData(form);
//         fetch('/complete_task', {
//             method: 'POST',
//             body: formData
//         })
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error('Network response was not ok');
//             }
//             return response.json();
//         })
//         .then(data => {
//             console.log('Success:', data);
//             location.reload();  // Reload the page to reflect changes
//         })
//         .catch(error => {
//             console.error('There was a problem with your fetch operation:', error);
//         });
//     }
// }

// console.log('Script loaded successfully.');


// function completeTask(checkbox) {
//     if (checkbox.checked) {
//         var form = document.getElementById('complete_tasks_form');
//         var formData = new FormData(form);

//         fetch('/complete_task', {
//             method: 'POST',
//             body: formData
//         }).then(response => {
//             if (response.ok) {
//                 location.reload();  // Reload the page to show updated status
//             }
//         });
//     }
// }
