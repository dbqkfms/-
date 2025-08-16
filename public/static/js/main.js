/**
 * THISGLOBAL Website JavaScript
 * Based on JSolution functionality
 */

(function() {
    'use strict';

    // ========================================
    // Mobile Menu Toggle
    // ========================================
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const navMobile = document.querySelector('.nav-mobile');
    const hasSubmenu = document.querySelectorAll('.has-submenu');

    if (mobileMenuToggle && navMobile) {
        mobileMenuToggle.addEventListener('click', function() {
            this.classList.toggle('active');
            navMobile.classList.toggle('active');
            document.body.style.overflow = navMobile.classList.contains('active') ? 'hidden' : '';
        });

        // Handle submenu toggles
        hasSubmenu.forEach(item => {
            const link = item.querySelector('a');
            link.addEventListener('click', function(e) {
                if (window.innerWidth <= 768) {
                    e.preventDefault();
                    item.classList.toggle('active');
                }
            });
        });
    }

    // Close mobile menu when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.header') && navMobile && navMobile.classList.contains('active')) {
            mobileMenuToggle.classList.remove('active');
            navMobile.classList.remove('active');
            document.body.style.overflow = '';
        }
    });

    // ========================================
    // Hero Slider
    // ========================================
    class HeroSlider {
        constructor() {
            this.slides = document.querySelectorAll('.slide');
            this.prevBtn = document.querySelector('.slider-prev');
            this.nextBtn = document.querySelector('.slider-next');
            this.indicators = document.querySelectorAll('.indicator');
            this.currentSlide = 0;
            this.slideInterval = null;
            
            if (this.slides.length > 0) {
                this.init();
            }
        }

        init() {
            // Add event listeners
            if (this.prevBtn) {
                this.prevBtn.addEventListener('click', () => this.prevSlide());
            }
            
            if (this.nextBtn) {
                this.nextBtn.addEventListener('click', () => this.nextSlide());
            }
            
            // Indicator clicks
            this.indicators.forEach((indicator, index) => {
                indicator.addEventListener('click', () => this.goToSlide(index));
            });
            
            // Start auto-play
            this.startAutoPlay();
            
            // Pause on hover
            const heroSection = document.querySelector('.hero');
            if (heroSection) {
                heroSection.addEventListener('mouseenter', () => this.stopAutoPlay());
                heroSection.addEventListener('mouseleave', () => this.startAutoPlay());
            }
        }

        updateSlide() {
            // Remove active class from all slides and indicators
            this.slides.forEach(slide => slide.classList.remove('active'));
            this.indicators.forEach(indicator => indicator.classList.remove('active'));
            
            // Add active class to current slide and indicator
            this.slides[this.currentSlide].classList.add('active');
            if (this.indicators[this.currentSlide]) {
                this.indicators[this.currentSlide].classList.add('active');
            }
        }

        nextSlide() {
            this.currentSlide = (this.currentSlide + 1) % this.slides.length;
            this.updateSlide();
        }

        prevSlide() {
            this.currentSlide = (this.currentSlide - 1 + this.slides.length) % this.slides.length;
            this.updateSlide();
        }

        goToSlide(index) {
            this.currentSlide = index;
            this.updateSlide();
        }

        startAutoPlay() {
            this.stopAutoPlay(); // Clear any existing interval
            this.slideInterval = setInterval(() => this.nextSlide(), 5000);
        }

        stopAutoPlay() {
            if (this.slideInterval) {
                clearInterval(this.slideInterval);
                this.slideInterval = null;
            }
        }
    }

    // Initialize slider
    const heroSlider = new HeroSlider();

    // ========================================
    // Smooth Scroll
    // ========================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            const href = this.getAttribute('href');
            if (href !== '#' && href !== '#0') {
                const target = document.querySelector(href);
                if (target) {
                    e.preventDefault();
                    const headerHeight = document.querySelector('.header').offsetHeight;
                    const targetPosition = target.getBoundingClientRect().top + window.pageYOffset - headerHeight;
                    
                    window.scrollTo({
                        top: targetPosition,
                        behavior: 'smooth'
                    });
                    
                    // Close mobile menu if open
                    if (navMobile && navMobile.classList.contains('active')) {
                        mobileMenuToggle.classList.remove('active');
                        navMobile.classList.remove('active');
                        document.body.style.overflow = '';
                    }
                }
            }
        });
    });

    // ========================================
    // Header Scroll Effect
    // ========================================
    let lastScroll = 0;
    const header = document.querySelector('.header');
    
    window.addEventListener('scroll', () => {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 100) {
            header.style.boxShadow = '0 2px 20px rgba(0, 0, 0, 0.1)';
        } else {
            header.style.boxShadow = '0 2px 10px rgba(0, 0, 0, 0.1)';
        }
        
        lastScroll = currentScroll;
    });

    // ========================================
    // Partners Slider (Infinite Loop)
    // ========================================
    const partnersTrack = document.querySelector('.partners-track');
    if (partnersTrack) {
        // Clone partners for infinite scroll
        const partners = partnersTrack.innerHTML;
        partnersTrack.innerHTML = partners + partners;
    }

    // ========================================
    // Contact Form Handler
    // ========================================
    const contactForm = document.getElementById('contactForm');
    const successModal = document.getElementById('successModal');
    const modalClose = document.querySelector('.modal-close');
    
    if (contactForm) {
        contactForm.addEventListener('submit', async function(e) {
            e.preventDefault();
            
            // Get form data
            const formData = new FormData(this);
            const data = {};
            formData.forEach((value, key) => {
                data[key] = value;
            });
            
            // Simulate form submission (replace with actual API call)
            try {
                // Show loading state
                const submitBtn = this.querySelector('.btn-submit');
                const originalText = submitBtn.innerHTML;
                submitBtn.innerHTML = '<span>전송 중...</span> <i class="fas fa-spinner fa-spin"></i>';
                submitBtn.disabled = true;
                
                // Simulate API call
                await new Promise(resolve => setTimeout(resolve, 1500));
                
                // In production, replace with actual API call:
                // const response = await fetch('/api/contact', {
                //     method: 'POST',
                //     headers: { 'Content-Type': 'application/json' },
                //     body: JSON.stringify(data)
                // });
                
                // Reset form
                this.reset();
                
                // Show success modal
                if (successModal) {
                    successModal.classList.add('active');
                }
                
                // Reset button
                submitBtn.innerHTML = originalText;
                submitBtn.disabled = false;
                
            } catch (error) {
                console.error('Form submission error:', error);
                alert('문의 전송 중 오류가 발생했습니다. 다시 시도해주세요.');
            }
        });
    }
    
    // Close modal
    if (modalClose) {
        modalClose.addEventListener('click', function() {
            successModal.classList.remove('active');
        });
    }
    
    // Close modal on outside click
    if (successModal) {
        successModal.addEventListener('click', function(e) {
            if (e.target === this) {
                this.classList.remove('active');
            }
        });
    }

    // ========================================
    // Intersection Observer for Animations
    // ========================================
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '0';
                entry.target.style.transform = 'translateY(30px)';
                
                setTimeout(() => {
                    entry.target.style.transition = 'all 0.6s ease';
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }, 100);
                
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);
    
    // Observe elements
    document.querySelectorAll('.product-card, .info-card').forEach(el => {
        observer.observe(el);
    });

    // ========================================
    // Lazy Loading Images
    // ========================================
    const lazyImages = document.querySelectorAll('img[data-src]');
    
    if ('IntersectionObserver' in window && lazyImages.length > 0) {
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    imageObserver.unobserve(img);
                }
            });
        });
        
        lazyImages.forEach(img => imageObserver.observe(img));
    }

    // ========================================
    // Initialize on DOM Content Loaded
    // ========================================
    document.addEventListener('DOMContentLoaded', function() {
        // Add any additional initialization here
        console.log('THISGLOBAL Website Initialized');
    });

})();