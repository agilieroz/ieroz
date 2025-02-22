document.addEventListener('DOMContentLoaded', () => {
    const toggleSidebar = document.getElementById('toggleSidebar');
    const sidebar = document.getElementById('sidebar');
    const overlay = document.getElementById('overlay');
    const mainContent = document.querySelector('main');

    // Fungsi buka/tutup sidebar
    toggleSidebar.addEventListener('click', () => {
        sidebar.classList.toggle('active');
        overlay.style.display = sidebar.classList.contains('active') ? 'block' : 'none';
    });

    // Klik overlay untuk menutup sidebar
    overlay.addEventListener('click', () => {
        sidebar.classList.remove('active');
        overlay.style.display = 'none';
    });

    // Animasi fade-in saat halaman dimuat
    window.addEventListener('load', () => {
        mainContent.style.opacity = '1';
        mainContent.style.transform = 'translateY(0)';
    });

    window.addEventListener('load', () => {
        document.querySelector('.fade-in').classList.add('show');
    });
    
    // === ANIMASI TYPING ===
    function typeEffect(element, text, speed, callback) {
        let i = 0;
        function typing() {
            if (i < text.length) {
                element.innerHTML += text.charAt(i);
                i++;
                setTimeout(typing, speed);
            } else if (callback) {
                setTimeout(callback, 500); // jeda sebelum mengetik teks berikutnya
            }
        }
        typing();
    }

    window.addEventListener('load', () => {
        const nameElement = document.getElementById("typing-name");
        const textElement = document.getElementById("typing-text");

        typeEffect(nameElement, "Agil Sieroz", 100, function () {
            textElement.classList.add("typing");
            typeEffect(textElement, "Sistem pemerintahan yang kacau. Sudah di demo, di debat, dan di kritik, tapi tidak ada evaluasi dan eksekusinya nol.", 50);
            typeEffect(textElement, "BANGSA INI PENAKUT UNTUK BERUBAH #INDONESIAGELAP", 50);
        });
    });

    // Animasi Partikel dengan Three.js
    const scene = new THREE.Scene();
    const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
    const renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('particleCanvas'), alpha: true });
    renderer.setSize(window.innerWidth, window.innerHeight);
    document.body.appendChild(renderer.domElement);

    // Partikel
    const particlesGeometry = new THREE.BufferGeometry();
    const particlesCount = 1000;
    const posArray = new Float32Array(particlesCount * 3);

    for (let i = 0; i < particlesCount * 3; i++) {
        posArray[i] = (Math.random() - 0.5) * 10;
    }

    particlesGeometry.setAttribute('position', new THREE.BufferAttribute(posArray, 3));

    const particlesMaterial = new THREE.PointsMaterial({
        size: 0.02,
        color: 0xffffff,
        transparent: true,
        opacity: 0.8
    });

    const particlesMesh = new THREE.Points(particlesGeometry, particlesMaterial);
    scene.add(particlesMesh);

    camera.position.z = 5;

    function animateParticles() {
        requestAnimationFrame(animateParticles);
        particlesMesh.rotation.y += 0.0005;
        particlesMesh.rotation.x += 0.0003;
        renderer.render(scene, camera);
    }
    animateParticles();
});
