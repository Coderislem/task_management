// image_profile_target.js
document.addEventListener('DOMContentLoaded', function() {
    const imageInput = document.getElementById('id_image_profile');
    const avatarPreview = document.getElementById('avatar-preview');

    imageInput.addEventListener('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                avatarPreview.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }
    });
});