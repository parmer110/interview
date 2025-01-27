CREATE TABLE records (
    id SERIAL PRIMARY KEY,
    data TEXT,
    date TIMESTAMP
);

INSERT INTO records (data, date) VALUES
('Sample data 1', '2023-01-01'),
('Sample data 2', '2023-02-01'),
('Sample data 3', '2023-03-01');