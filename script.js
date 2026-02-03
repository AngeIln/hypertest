const banana = document.getElementById("banana");

const onMove = (event) => {
  const bounds = banana.getBoundingClientRect();
  const relX = (event.clientX - bounds.left) / bounds.width - 0.5;
  const relY = (event.clientY - bounds.top) / bounds.height - 0.5;
  banana.style.transform = `rotate(${relX * 12 - 12}deg) translate(${relX * 12}px, ${relY * 8}px)`;
};

const reset = () => {
  banana.style.transform = "rotate(-12deg) translate(0, 0)";
};

banana.addEventListener("mousemove", onMove);
banana.addEventListener("mouseleave", reset);
