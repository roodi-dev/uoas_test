// Modal functionality for Learn More buttons
const learnMoreButtons = document.querySelectorAll('.learn-more-btn[data-modal-target]');
const modals = document.querySelectorAll('.modal');

function trapFocus(element) {
    const focusableElements = element.querySelectorAll('a[href], button:not([disabled]), textarea, input, select, [tabindex]:not([tabindex="-1"])');
    const firstFocusable = focusableElements[0];
    const lastFocusable = focusableElements[focusableElements.length - 1];

    element.addEventListener('keydown', (e) => {
        if (e.key === 'Tab') {
            if (e.shiftKey) { // Shift + Tab
                if (document.activeElement === firstFocusable) {
                    e.preventDefault();
                    lastFocusable.focus();
                }
            } else { // Tab
                if (document.activeElement === lastFocusable) {
                    e.preventDefault();
                    firstFocusable.focus();
                }
            }
        }
    });
}

learnMoreButtons.forEach(button => {
    button.addEventListener('click', () => {
        const modalId = button.getAttribute('data-modal-target');
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.setAttribute('aria-hidden', 'false');
            modal.classList.add('show');
            // Focus the modal for accessibility
            modal.querySelector('.modal-close').focus();
            trapFocus(modal);
        }
    });
});

modals.forEach(modal => {
    const closeButton = modal.querySelector('.modal-close');
    closeButton.addEventListener('click', () => {
        modal.setAttribute('aria-hidden', 'true');
        modal.classList.remove('show');
    });

    // Close modal on Escape key press
    modal.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            modal.setAttribute('aria-hidden', 'true');
            modal.classList.remove('show');
        }
    });
});

// Close modal if clicked outside modal content
modals.forEach(modal => {
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.setAttribute('aria-hidden', 'true');
            modal.classList.remove('show');
        }
    });
});

