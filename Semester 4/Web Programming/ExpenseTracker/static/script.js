document.addEventListener('DOMContentLoaded', function() {
    // File Upload Handling
    const fileInput = document.getElementById('fileInput');
    const dropZone = document.getElementById('dropZone');
    const uploadBtn = document.getElementById('uploadBtn');
    const uploadForm = document.getElementById('uploadForm');
    const loadingState = document.getElementById('loadingState');
    const dropText = document.querySelector('.drop-text');

    if (fileInput && dropZone) {
        // Handle drag and drop events
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            dropZone.addEventListener(eventName, preventDefaults, false);
        });

        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }

        ['dragenter', 'dragover'].forEach(eventName => {
            dropZone.addEventListener(eventName, () => {
                dropZone.classList.add('dragover');
            }, false);
        });

        ['dragleave', 'drop'].forEach(eventName => {
            dropZone.addEventListener(eventName, () => {
                dropZone.classList.remove('dragover');
            }, false);
        });

        dropZone.addEventListener('drop', (e) => {
            const dt = e.dataTransfer;
            const files = dt.files;
            fileInput.files = files;
            handleFiles(files);
        }, false);

        fileInput.addEventListener('change', function() {
            handleFiles(this.files);
        });

        function handleFiles(files) {
            if (files.length > 0) {
                const file = files[0];
                if (file.name.endsWith('.csv')) {
                    dropText.textContent = `Selected: ${file.name}`;
                    uploadBtn.disabled = false;
                } else {
                    dropText.textContent = 'Please select a valid CSV file.';
                    dropText.style.color = '#f87171';
                    uploadBtn.disabled = true;
                }
            }
        }

        if (uploadForm) {
            uploadForm.addEventListener('submit', function() {
                uploadForm.style.display = 'none';
                loadingState.classList.remove('hidden');
            });
        }
    }

    // Chart.js Initialization
    const chartCanvas = document.getElementById('expenseChart');
    if (chartCanvas) {
        fetch('/api/chart-data')
            .then(response => response.json())
            .then(data => {
                const ctx = chartCanvas.getContext('2d');
                
                // Color palette for chart
                const colors = [
                    '#6366f1', // Indigo
                    '#8b5cf6', // Violet
                    '#ec4899', // Pink
                    '#10b981', // Emerald
                    '#f59e0b', // Amber
                    '#3b82f6', // Blue
                    '#64748b'  // Slate
                ];

                new Chart(ctx, {
                    type: 'doughnut',
                    data: {
                        labels: data.labels,
                        datasets: [{
                            data: data.values,
                            backgroundColor: colors,
                            borderWidth: 0,
                            hoverOffset: 4
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: {
                                position: 'bottom',
                                labels: {
                                    color: '#f8fafc',
                                    padding: 20,
                                    font: {
                                        family: "'Inter', sans-serif",
                                        size: 12
                                    }
                                }
                            },
                            tooltip: {
                                backgroundColor: 'rgba(15, 23, 42, 0.9)',
                                titleColor: '#f8fafc',
                                bodyColor: '#f8fafc',
                                padding: 12,
                                cornerRadius: 8,
                                displayColors: true,
                                callbacks: {
                                    label: function(context) {
                                        let label = context.label || '';
                                        if (label) {
                                            label += ': ';
                                        }
                                        if (context.parsed !== null) {
                                            label += new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(context.parsed);
                                        }
                                        return label;
                                    }
                                }
                            }
                        },
                        cutout: '75%',
                        animation: {
                            animateScale: true,
                            animateRotate: true
                        }
                    }
                });
            })
            .catch(error => console.error('Error fetching chart data:', error));
    }
});
