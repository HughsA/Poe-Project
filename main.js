const fontSizeButton = document.getElementById("fontSizeButton");
const body = document.body;

fontSizeButton.addEventListener("click", function() {
    body.classList.toggle("large-font");
});

const button =document.getElementById('aboutButton');
const hoverMessage = document.querySelector('.hover-message');

button.addEventListener('mouseover', () => {
    hoverMessage.style.display = 'block';
});

button.addEventListener('mouseout', () => {
    hoverMessage.style.display = 'none';
});

button.addEventListener('click', () => {
    if (hoverMessage.style.display === 'block') {
      hoverMessage.style.display = 'none';
    } else {
      hoverMessage.style.display = 'block';
    }
  });
