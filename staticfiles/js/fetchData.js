// amounts = [];
// transactionTime = [];
// const d = new Date();
// TodayDate = (d.getDate());
// dayCount = 0
// $dayCount = document.getElementById("dayCount")
// console.log($dayCount);

// getData();
// async function getData() {
//     if (TodayDate >= 1) {
//         console.log(TodayDate + " date");
//         const response = await fetch("http://127.0.0.1:8000/todayGraph/" + TodayDate);
//         const data = await response.json();
//         length = data.amounts.length;
//         console.log(data.amounts.length);
//         amounts = amounts.slice(0, 0).concat(data.amounts).concat(amounts.slice(0))
//         transactionTime = transactionTime.slice(0, 0).concat(data.transactionTime).concat(transactionTime.slice(0))

//         new Chart(document.getElementById("myAreaChart"), {
//             type: 'line',
//             data: {
//                 labels: transactionTime,
//                 datasets: [
//                     {
//                         label: "Amount",
//                         backgroundColor: '#4E73DF',
//                         data: amounts
//                     }
//                 ]
//             },
//             options: {
//                 responsive: true,
//                 legend: { display: false },
//                 title: {
//                     display: true,
//                 }
//             }
//         });
//         document.getElementById("dayCount").innerHTML = dayCount;
//         dayCount++
//         --TodayDate;
//     }
//     else {
//         return;
//     }
// }
