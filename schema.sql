CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    modstatus BOOL
);

CREATE TABLE topics (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    topic_id INTEGER REFERENCES topics,
    user_id INTEGER REFERENCES users,
    content TEXT,
    time_sent TIMESTAMP
);

CREATE TABLE likes (
    user_id INTEGER REFERENCES users,
    message_id INTEGER REFERENCES messages
);