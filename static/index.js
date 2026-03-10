document.body.classList.add('loading');

document.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    const preloader = document.getElementById('preloader');
    preloader.classList.add('hidden');
    document.body.classList.remove('loading');
  }, 1900);
});

const themeToggle = document.getElementById('themeToggle');


const savedTheme = localStorage.getItem('snapforge-theme');
if (savedTheme === 'dark') {
  document.documentElement.classList.add('dark');
  themeToggle.checked = true;
}


themeToggle.addEventListener('change', () => {
  if (themeToggle.checked) {
    document.documentElement.classList.add('dark');
    localStorage.setItem('snapforge-theme', 'dark');
  } else {
    document.documentElement.classList.remove('dark');
    localStorage.setItem('snapforge-theme', 'light');
  }
});

let collectedPhotos = [];


window.takePhoto = function() {
  const numPhotos = parseInt(document.getElementById('numPhotos').value);
  document.getElementById('captureBtn').disabled = true;
  document.getElementById('downloadBtn').disabled = true;
  collectedPhotos = [];

  const container = document.getElementById('photoRectangles');
  container.innerHTML = '';
  
  for (let i = 0; i < numPhotos; i++) {
    const rect = document.createElement('div');
    rect.className = 'photo-rectangle';
    rect.id = `rect-${i}`;
    rect.textContent = `Photo ${i + 1}`;
    container.appendChild(rect);
  }

  captureSequence(numPhotos, 0);
};

function captureSequence(numPhotos, photoIndex) {
  if (photoIndex >= numPhotos) {
    makeCollage(collectedPhotos);
    return;
  }

  const currentRect = document.getElementById(`rect-${photoIndex}`);
  currentRect.classList.add('active');

  let countdown = 3;
  const countdownDiv = document.getElementById('countdown');
  countdownDiv.style.display = 'block';
  countdownDiv.textContent = countdown;

  const countdownInterval = setInterval(() => {
    countdown--;
    if (countdown > 0) {
      countdownDiv.textContent = countdown;
    } else {
      clearInterval(countdownInterval);
      countdownDiv.style.display = 'none';

      const flash = document.getElementById('flash');
      flash.classList.add('active');
      setTimeout(() => flash.classList.remove('active'), 300);

      fetch('/capture?num_photos=1')
        .then(res => res.blob())
        .then(blob => {
          const img = new Image();
          img.onload = () => {
            collectedPhotos.push(img);
            currentRect.classList.remove('active');
            currentRect.classList.add('captured');
            setTimeout(() => captureSequence(numPhotos, photoIndex + 1), 500);
          };
          img.src = URL.createObjectURL(blob);
        });
    }
  }, 1000);
}

function makeCollage(images) {
  if (images.length === 0) return;
  const count = images.length;
  const w = images[0].width;
  const h = images[0].height;
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');

  if (count === 6) {
    canvas.width = w * 3; canvas.height = h * 2;
    images.forEach((img, i) => ctx.drawImage(img, (i % 3) * w, Math.floor(i / 3) * h, w, h));
  } else if (count === 4) {
    canvas.width = w * 2; canvas.height = h * 2;
    images.forEach((img, i) => ctx.drawImage(img, (i % 2) * w, Math.floor(i / 2) * h, w, h));
  } else if (count === 3) {
    canvas.width = w * 3; canvas.height = h;
    images.forEach((img, i) => ctx.drawImage(img, i * w, 0, w, h));
  } else if (count === 2) {
    canvas.width = w * 2; canvas.height = h;
    images.forEach((img, i) => ctx.drawImage(img, i * w, 0, w, h));
  }

  const dataUrl = canvas.toDataURL('image/jpeg');
  const resultImg = document.getElementById('result');
  resultImg.src = dataUrl;
  resultImg.style.display = 'block';
  
  document.getElementById('emptyState').style.display = 'none';
  document.getElementById('photoRectangles').innerHTML = '';
  document.getElementById('captureBtn').disabled = false;
  document.getElementById('downloadBtn').disabled = false;
}


window.downloadPhoto = function() {
  const img = document.getElementById('result').src;
  const a = document.createElement('a');
  a.href = img;
  a.download = 'collage.jpg';
  a.click();
};