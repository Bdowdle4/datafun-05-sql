-- 2. insert_records.sql - insert at least 10 additional records into each table.

-- inserts the following data into authors
INSERT INTO authors (author_id, first_name, last_name) VALUES
('10f88232-2bf8-4d88-a6a2-dfcebb22a596', 'Arthur', 'Conan Doyle'),
('c3a47e85-3b7c-4196-a7a8-8b55d8fc1f70', 'James', 'Hogg'),
('e0b75863-977e-4db4-85c7-df9bb8ee6dab', 'Bram', 'Stoker'),
('7b144e32-8gg5-4b58-8eb0-e63d3c9f9b8d', 'Emily', 'Bronte'),
('ba5bb514-257e-4d45-b83d-0dcebb22a596', 'Franz', 'Kafka'),
('de1e8f17-7b4c-49f4-bb75-4baaacff8a10', 'Ray', 'Bradbury'),
('3b6e3f0d-cd98-4b73-94a7-0841a3f446c8', 'Sylvia', 'Plath'),
('4b4a7a5b-4674-499e-83b7-5b8b4a6c1e6b', 'Edgar', 'Allen Poe'),
('5c3f8f2e-e9b4-4faa-88f1-5b8b4a6c1e6b', 'H.P.', 'Lovecraft'),
('1b3f5d8e-2b4e-4efa-ba9e-5b8b4a6c1e6b', 'Virginia', 'Woolf'),

-- inserts the following data into books
INSERT INTO books (book_id, title, year_published, author_id) VALUES
('d6f83870-gg32-4a5d-90ab-26a49ab6ed12', 'A Study in Scarlet', '1887', '10f88232-2bf8-4d88-a6a2-dfcebb22a596')
('0f5f44f7-55e9-4f49-b8c4-c64d847587d3', 'The Mysterious Bride', '1800', 'c3a47e85-3b7c-4196-a7a8-8b55d8fc1f70')
('f9d9e7de-d55e-4d1d-b3ab-59343bf32bc2', 'Dracula', '1897', 'e0b75863-977e-4db4-85c7-df9bb8ee6dab')
('38e530f1-339e-4d6e-a587-2ed4d6c44e9c', 'Wuthering Heights', '1847', '7b144e32-8gg5-4b58-8eb0-e63d3c9f9b8d')
('ba5bb514-257e-4d45-b83d-0dcebb22a596', 'The Metamorphos', '1915', 'c2a62a4b-de6d-4246-9bf7-b2601d542e6d')
('f9d9e7de-d55e-4d1d-b3ab-59343bf32bc2', 'Farenheit 451' '1953', 'de1e8f17-7b4c-49f4-bb75-4baaacff8a10')
('c6e67918-f610-4a6b-bc3a-979f6ad802f0', 'Lady Lazarus', '1965', '3b6e3f0d-cd98-4b73-94a7-0841a3f446c8')
('be951205-7dd3-4b3d-96f1-7257b8fc8c0f', 'The Fall of the House of Usher', '1839', '4b4a7a5b-4674-499e-83b7-5b8b4a6c1e6b')
('dce0f8f2-e4fe-48a9-b8ff-960b6baf1f6f', 'At the Mountains of Madness', '1936', '5c3f8f2e-e9b4-4faa-88f1-5b8b4a6c1e6b')
('ca8e64c3-2f78-47f5-82cc-3e4e30f63b75', 'Mrs Dalloway', '1925', '1b3f5d8e-2b4e-4efa-ba9e-5b8b4a6c1e6b')