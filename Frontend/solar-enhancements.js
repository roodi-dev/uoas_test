/**
 * Enhanced Slideshow Functionality for Solar Projects
 */
let currentSlide = 0;
let slides = document.querySelectorAll('.slide');
let isPlaying = true;
let slideInterval;

function updateSlideshow() {
    const slider = document.querySelector('.projects-slider');
    if (!slider || slides.length === 0) return;
    const slideWidth = slides[0].offsetWidth;
    slider.style.transform = `translateX(-${currentSlide * slideWidth}px)`;

    // Update indicators
    document.querySelectorAll('.indicator').forEach((indicator, index) => {
        indicator.classList.toggle('active', index === currentSlide);
    });
}

function nextSlide() {
    currentSlide = (currentSlide + 1) % slides.length;
    updateSlideshow();
}

function previousSlide() {
    currentSlide = (currentSlide - 1 + slides.length) % slides.length;
    updateSlideshow();
}

function goToSlide(slideIndex) {
    currentSlide = slideIndex;
    updateSlideshow();
}

function toggleSlideshow() {
    const playPauseBtn = document.getElementById('play-pause-btn');
    isPlaying = !isPlaying;

    if (isPlaying) {
        startSlideshow();
        playPauseBtn.textContent = '⏸️';
    } else {
        stopSlideshow();
        playPauseBtn.textContent = '▶️';
    }
}

function startSlideshow() {
    slideInterval = setInterval(nextSlide, 4000);
}

function stopSlideshow() {
    clearInterval(slideInterval);
}

// Solution Modal Functionality
function openSolutionModal(solutionType) {
    const modal = document.getElementById('solution-modal');
    const modalContent = document.getElementById('modal-content');

    const solutions = {
        standard: {
            title: 'Standard Home Solar System',
            description: 'Perfect for the average South African household looking to reduce electricity costs and achieve energy independence.',
            features: [
                '3-5kW Solar Panel System',
                '5kWh Battery Storage',
                'Hybrid Inverter with MPPT',
                '25-year Performance Warranty',
                'Monitoring System Included',
                'Professional Installation'
            ],
            price: 'From R85,000',
            roi: '4-5 year payback period'
        },
        tailored: {
            title: 'Tailored Home Solar System',
            description: 'Custom-designed solar solutions for unique home requirements, high energy usage, or specific architectural constraints.',
            features: [
                'Custom System Design',
                'High-Capacity Panels (5-10kW)',
                'Extended Battery Storage',
                'Smart Home Integration',
                'Advanced Monitoring',
                'Flexible Installation Options'
            ],
            price: 'From R120,000',
            roi: '3-4 year payback period'
        },
        commercial: {
            title: 'Commercial Solar Solutions',
            description: 'Large-scale solar installations designed for businesses, warehouses, and commercial properties.',
            features: [
                '50kW+ Solar Systems',
                'Commercial Battery Storage',
                'Three-Phase Inverters',
                'Advanced Monitoring Platform',
                'Tax Incentive Optimization',
                'Maintenance Contracts'
            ],
            price: 'Custom Quote Required',
            roi: '4-6 year payback period'
        },
        independence: {
            title: 'Energy Independence Solutions',
            description: 'Complete energy independence packages for businesses wanting to break free from Eskom\'s rising costs.',
            features: [
                'Full Off-Grid Capability',
                'Large Battery Storage Systems',
                'Backup Generator Integration',
                '24/7 Power Guarantee',
                'Remote Monitoring',
                'Emergency Power Systems'
            ],
            price: 'Custom Quote Required',
            roi: '3-5 year payback period'
        },
        future: {
            title: 'Future-Ready Solar Systems',
            description: 'Scalable solar systems designed for future expansion and technological advancements.',
            features: [
                'Modular Panel Design',
                'Expandable Battery System',
                'Smart Grid Integration',
                'IoT Monitoring Platform',
                'Easy System Upgrades',
                'Future-Proof Technology'
            ],
            price: 'From R95,000 (Base System)',
            roi: '4-6 year payback period'
        }
    };

    const solution = solutions[solutionType];
    modalContent.innerHTML = `
        <h2>${solution.title}</h2>
        <p>${solution.description}</p>
        <h3>Key Features:</h3>
        <ul>
            ${solution.features.map(feature => `<li>${feature}</li>`).join('')}
        </ul>
        <div style="background: #f0f8ff; padding: 20px; border-radius: 10px; margin: 20px 0;">
            <h3 style="margin-top: 0; color: #005a99;">Investment Details</h3>
            <p><strong>Starting Price:</strong> ${solution.price}</p>
            <p><strong>Expected ROI:</strong> ${solution.roi}</p>
        </div>
        <button onclick="closeSolutionModal(); document.querySelector('.solar-contact-form').scrollIntoView();" style="background: #005a99; color: white; border: none; padding: 12px 24px; border-radius: 8px; cursor: pointer; font-size: 1rem;">
            Get Quote for This System
        </button>
    `;

    modal.style.display = 'block';
}

function closeSolutionModal() {
    document.getElementById('solution-modal').style.display = 'none';
}

// Initialize slideshow when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    if (slides.length > 0) {
        updateSlideshow();
        startSlideshow();

        // Add indicators
        const indicators = document.querySelectorAll('.indicator');
        indicators.forEach((indicator, index) => {
            if (index === 0) indicator.classList.add('active');
        });
    }

    // Close modal when clicking outside
    window.onclick = function(event) {
        const modal = document.getElementById('solution-modal');
        if (event.target === modal) {
            closeSolutionModal();
        }
    };
});
