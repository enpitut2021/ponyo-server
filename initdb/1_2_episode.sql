-- task_idがリレーションとなる
-- 中身・・・アサイン、タスクの詳細（ネストされたタスクも実現する）
CREATE TABLE episodes (
    id TEXT NOT NULL UNIQUE,
    description TEXT NOT NULL DEFAULT '',
    user_id TEXT NOT NULL DEFAULT 'example-user-id',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT current_timestamp,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT current_timestamp,
    CONSTRAINT episode_pkey PRIMARY KEY(id)
);
INSERT INTO episodes(id, description, user_id)
VALUES('exapmle-episode-id-1','私はチャックを開けたまま外を歩いていました', 'example-user-id');
INSERT INTO episodes(id, description, user_id)
VALUES('exapmle-episode-id-2','私はチャックを開けたまま外を歩いていました', 'example-user-id-1');
INSERT INTO episodes(id, description, user_id)
VALUES('exapmle-episode-id-3','私はチャックを開けたまま外を歩いていました', 'example-user-id-2');
