/**
 * THIS GLOBAL - Main JavaScript
 * Modern, clean interactions
 */

(function() {
    'use strict';

    // ========================================
    // Initialize
    // ========================================
    document.addEventListener('DOMContentLoaded', function() {
        initHeader();
        initMobileMenu();
        initLanguageToggle();
        initContactForm();
        initLazyLoading();
        initScrollAnimations();
        console.log('THIS GLOBAL website initialized');
    });

    // ========================================
    // Header Scroll Effect
    // ========================================
    function initHeader() {
        const header = document.getElementById('header');
        let lastScroll = 0;

        window.addEventListener('scroll', () => {
            const currentScroll = window.pageYOffset;
            
            // Add scrolled class for styling
            if (currentScroll > 50) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }

            // Hide/show header on scroll
            if (currentScroll > lastScroll && currentScroll > 100) {
                header.style.transform = 'translateY(-100%)';
            } else {
                header.style.transform = 'translateY(0)';
            }

            lastScroll = currentScroll;
        });
    }

    // ========================================
    // Mobile Menu
    // ========================================
    function initMobileMenu() {
        const toggle = document.getElementById('mobileMenuToggle');
        const nav = document.getElementById('navMobile');
        const submenus = document.querySelectorAll('.has-submenu');

        if (!toggle || !nav) return;

        // Toggle mobile menu
        toggle.addEventListener('click', function() {
            this.classList.toggle('active');
            nav.classList.toggle('active');
            document.body.style.overflow = nav.classList.contains('active') ? 'hidden' : '';
        });

        // Handle submenu toggles
        submenus.forEach(item => {
            const link = item.querySelector('a');
            link.addEventListener('click', function(e) {
                if (window.innerWidth <= 768) {
                    e.preventDefault();
                    item.classList.toggle('active');
                }
            });
        });

        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!e.target.closest('.header')) {
                toggle.classList.remove('active');
                nav.classList.remove('active');
                document.body.style.overflow = '';
            }
        });

        // Close menu on link click
        nav.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', function() {
                if (!this.parentElement.classList.contains('has-submenu')) {
                    toggle.classList.remove('active');
                    nav.classList.remove('active');
                    document.body.style.overflow = '';
                }
            });
        });
    }

    // ========================================
    // Language Toggle
    // ========================================
    function initLanguageToggle() {
        const langToggle = document.getElementById('langToggle');
        if (!langToggle) return;

        const langOptions = langToggle.querySelectorAll('.lang-option');
        
        langOptions.forEach(option => {
            option.addEventListener('click', function() {
                const lang = this.getAttribute('data-lang');
                
                // Update active state
                langOptions.forEach(opt => opt.classList.remove('active'));
                this.classList.add('active');
                
                // Update language
                if (window.i18n) {
                    window.i18n.setLanguage(lang);
                    document.body.className = lang;
                }
            });
        });

        // Set initial language
        const currentLang = localStorage.getItem('language') || 'ko';
        document.body.className = currentLang;
        langOptions.forEach(opt => {
            if (opt.getAttribute('data-lang') === currentLang) {
                opt.classList.add('active');
            } else {
                opt.classList.remove('active');
            }
        });
    }

    // ========================================
    // Contact Form
    // ========================================
    function initContactForm() {
        const form = document.getElementById('contactForm');
        if (!form) return;

        form.addEventListener('submit', async function(e) {
            e.preventDefault();

            // Get form data
            const formData = new FormData(this);
            const data = {};
            formData.forEach((value, key) => {
                data[key] = value;
            });

            // Get submit button
            const submitBtn = this.querySelector('.submit-btn');
            const originalContent = submitBtn.innerHTML;
            
            try {
                // Show loading state
                submitBtn.innerHTML = '<span>전송 중...</span> <i class="fas fa-spinner fa-spin"></i>';
                submitBtn.disabled = true;

                // Send to API
                const response = await fetch('/api/contact', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                });

                const result = await response.json();

                if (result.success) {
                    // Show success message
                    showNotification('문의가 성공적으로 접수되었습니다.', 'success');
                    form.reset();
                } else {
                    throw new Error(result.error || 'Failed to send');
                }

            } catch (error) {
                console.error('Form submission error:', error);
                showNotification('전송 중 오류가 발생했습니다. 다시 시도해주세요.', 'error');
            } finally {
                // Reset button
                submitBtn.innerHTML = originalContent;
                submitBtn.disabled = false;
            }
        });
    }

    // ========================================
    // Notification System
    // ========================================
    function showNotification(message, type = 'info') {
        // Create notification element
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.innerHTML = `
            <div class="notification-content">
                <i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-circle'}"></i>
                <span>${message}</span>
            </div>
        `;

        // Add styles
        const styles = document.createElement('style');
        styles.textContent = `
            .notification {
                position: fixed;
                top: 100px;
                right: 20px;
                padding: 16px 24px;
                background: white;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
                z-index: 9999;
                animation: slideIn 0.3s ease;
                max-width: 400px;
            }
            .notification-success {
                border-left: 4px solid #10b981;
            }
            .notification-error {
                border-left: 4px solid #ef4444;
            }
            .notification-content {
                display: flex;
                align-items: center;
                gap: 12px;
            }
            .notification-success i {
                color: #10b981;
            }
            .notification-error i {
                color: #ef4444;
            }
            @keyframes slideIn {
                from {
                    transform: translateX(100%);
                    opacity: 0;
                }
                to {
                    transform: translateX(0);
                    opacity: 1;
                }
            }
        `;
        document.head.appendChild(styles);

        // Add to page
        document.body.appendChild(notification);

        // Remove after 5 seconds
        setTimeout(() => {
            notification.style.animation = 'slideOut 0.3s ease';
            setTimeout(() => {
                notification.remove();
            }, 300);
        }, 5000);
    }

    // ========================================
    // Lazy Loading
    // ========================================
    function initLazyLoading() {
        const images = document.querySelectorAll('img[loading="lazy"]');
        
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries, observer) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.style.opacity = '0';
                        img.onload = function() {
                            img.style.transition = 'opacity 0.3s ease';
                            img.style.opacity = '1';
                        };
                        observer.unobserve(img);
                    }
                });
            }, {
                rootMargin: '50px 0px'
            });

            images.forEach(img => imageObserver.observe(img));
        }
    }

    // ========================================
    // Scroll Animations
    // ========================================
    function initScrollAnimations() {
        const animateElements = document.querySelectorAll('.product-card, .service-card, .special-item');
        
        if ('IntersectionObserver' in window) {
            const animateObserver = new IntersectionObserver((entries) => {
                entries.forEach((entry, index) => {
                    if (entry.isIntersecting) {
                        setTimeout(() => {
                            entry.target.style.opacity = '0';
                            entry.target.style.transform = 'translateY(20px)';
                            
                            setTimeout(() => {
                                entry.target.style.transition = 'all 0.6s ease';
                                entry.target.style.opacity = '1';
                                entry.target.style.transform = 'translateY(0)';
                            }, index * 50); // Stagger animation
                        }, 100);
                        
                        animateObserver.unobserve(entry.target);
                    }
                });
            }, {
                threshold: 0.1,
                rootMargin: '0px 0px -50px 0px'
            });

            animateElements.forEach(el => animateObserver.observe(el));
        }
    }

    // ========================================
    // Smooth Scroll
    // ========================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href === '#' || href === '#0') return;
            
            const target = document.querySelector(href);
            if (target) {
                e.preventDefault();
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // ========================================
    // Video Autoplay Management
    // ========================================
    const videos = document.querySelectorAll('video[autoplay]');
    videos.forEach(video => {
        // Ensure videos play on mobile
        video.setAttribute('playsinline', '');
        video.setAttribute('muted', '');
        
        // Play video when in viewport
        if ('IntersectionObserver' in window) {
            const videoObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.play().catch(e => console.log('Video autoplay failed:', e));
                    } else {
                        entry.target.pause();
                    }
                });
            }, {
                threshold: 0.5
            });
            
            videoObserver.observe(video);
        }
    });

})();