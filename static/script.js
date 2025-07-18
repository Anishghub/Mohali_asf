// const video = document.getElementById("video");
// navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
//   video.srcObject = stream;
// });

// function capture() {
//   const canvas = document.getElementById("canvas");
//   canvas.width = video.videoWidth;
//   canvas.height = video.videoHeight;
//   canvas.getContext("2d").drawImage(video, 0, 0);
//   canvas.toBlob(blob => {
//     const formData = new FormData();
//     formData.append("image", blob);
//     fetch("/mark", {
//       method: "POST",
//       body: formData
//     })
//     .then(res => res.json())
//     .then(data => {
//       document.getElementById("msg").innerText = data.message;
//     });
//   }, "image/jpeg");
// }

// IN & OUT 
// const video = document.getElementById("video");
// navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
//   video.srcObject = stream;
// });

// function capture(status) {
//   const canvas = document.getElementById("canvas");
//   canvas.width = video.videoWidth;
//   canvas.height = video.videoHeight;
//   const ctx = canvas.getContext("2d");
//   ctx.drawImage(video, 0, 0);

//   canvas.toBlob(blob => {
//     const formData = new FormData();
//     formData.append('image', blob);
//     formData.append('status', status);  // IN or OUT

//     fetch("/mark", {
//       method: "POST",
//       body: formData
//     })
//     .then(res => res.json())
//     .then(data => {
//       document.getElementById("msg").innerText = data.message;
//     });
//   }, 'image/jpeg');
// }

//  IN % OUT 

// DASHBOARD.... START 

const video = document.getElementById("video");
navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
  video.srcObject = stream;
});

function capture(status) {
  const canvas = document.getElementById("canvas");
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  const ctx = canvas.getContext("2d");
  ctx.drawImage(video, 0, 0);

  canvas.toBlob(blob => {
    const formData = new FormData();
    formData.append('image', blob);
    formData.append('status', status);

    fetch("/mark", {
      method: "POST",
      body: formData
    })
    .then(res => res.json())
    .then(data => {
      document.getElementById("msg").innerText = data.message;
    });
  }, 'image/jpeg');
}

function deleteEntry(index) {
  fetch(`/delete/${index}`, {
    method: "POST"
  }).then(() => {
    window.location.reload();
  });
}

// DASGBOARD ...END 
