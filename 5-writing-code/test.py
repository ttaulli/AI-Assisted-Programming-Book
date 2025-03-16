function displayUserComment(comment) {
  const commentSection = document.getElementById('comments');
  const p = document.createElement('p');
  p.textContent = comment;
  commentSection.appendChild(p);
}