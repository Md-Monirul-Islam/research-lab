function toggleText() {
    const dots = document.getElementById("dots");
    const moreText = document.getElementById("more");
    const readMoreBtn = document.getElementById("read-more");
  
    if (dots.style.display === "none") {
      dots.style.display = "inline";
      moreText.style.display = "none";
      readMoreBtn.innerHTML = "Read More";
    } else {
      dots.style.display = "none";
      moreText.style.display = "inline";
      readMoreBtn.innerHTML = "Read Less";
    }
  }
  