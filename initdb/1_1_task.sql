-- task_idがリレーションとなる
-- 中身・・・アサイン、タスクの詳細（ネストされたタスクも実現する）
CREATE TABLE tasks (
    id TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL DEFAULT '',
    description TEXT NOT NULL DEFAULT '',
    deadline TIMESTAMP WITH TIME ZONE DEFAULT current_timestamp,
    is_done boolean DEFAULT false,
    priority integer NOT NULL DEFAULT 0,
    user_id TEXT NOT NULL DEFAULT 'example-user-id',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT current_timestamp,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT current_timestamp,
    CONSTRAINT task_pkey PRIMARY KEY(id)
);
INSERT INTO tasks(id, name, description, user_id, deadline)
VALUES(
        'example-task-id-1',
        'テストタスク',
        'これはテストタスクです',
        'example-user-id',
        'Wed, 12 Jan 2022 08:20:34 JST'
    );
INSERT INTO tasks(id, name, description, user_id, deadline)
VALUES(
        'example-task-id-2',
        'テストタスク',
        'これはテストタスクです',
        'example-user-id-1',
        'Wed, 12 Jan 2022 08:20:34 JST'
    );
INSERT INTO tasks(id, name, description, user_id, deadline)
VALUES(
        'example-task-id-3',
        'テストタスク',
        'これはテストタスクです',
        'example-user-id-2',
        'Wed, 12 Jan 2022 08:20:34 JST'
    );