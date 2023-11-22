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

  // Function to open a popup with poem data
function openPopupWithData(poemTitle, poemData) {
  const popupWindow = window.open('', 'Poem Popup', 'width=600, height=400');
  popupWindow.document.write('<html><head><title>' + poemTitle + '</title></head><body>');
  popupWindow.document.write('<div class="popup"><h1>' + poemTitle + '</h1>');
  popupWindow.document.write('<p>' + poemData + '</p></div>'); // Display the poem data
  popupWindow.document.write('</body></html>');
}

// Function to fetch poem data and open popup
function fetchAndDisplayPoem(poemTitle) {
  fetch(`http://127.0.0.1:5000/poe_search?title=${encodeURIComponent(poemTitle)}`)
      .then(response => response.json())
      .then(data => {
          // Assuming 'data' contains the poem text or related information
          openPopupWithData(poemTitle, data);
      })
      .catch(error => console.error('Error:', error));
}

// Add event listener for submitting a poem title
const submitButton = document.getElementById('submitButton');
submitButton.addEventListener('click', function() {
  const poemTitle = document.getElementById('messageInput').value;
  fetchAndDisplayPoem(poemTitle);
});

// Add event listeners for selecting a poem title from the list
document.querySelectorAll('.poemTitle').forEach(item => {
  item.addEventListener('click', function() {
      const poemTitle = this.textContent;
      fetchAndDisplayPoem(poemTitle);
  });
});