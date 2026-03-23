-- Test data for analytics endpoints
-- Insert learners
INSERT INTO learner (external_id, student_group, enrolled_at) VALUES
    ('student-001', 'group-1', NOW()),
    ('student-002', 'group-1', NOW()),
    ('student-003', 'group-2', NOW()),
    ('student-004', 'group-2', NOW()),
    ('student-005', 'group-1', NOW())
ON CONFLICT (external_id) DO NOTHING;

-- Insert interactions for lab-01 tasks (parent_id=1, task ids: 8-16)
-- Task 8: Lab setup (5 attempts, 5 passed = 100%)
INSERT INTO interacts (learner_id, item_id, kind, score, checks_passed, checks_total, created_at) VALUES
    (1, 8, 'submission', 100.0, 2, 2, NOW() - INTERVAL '1 day'),
    (2, 8, 'submission', 100.0, 2, 2, NOW() - INTERVAL '1 day'),
    (3, 8, 'submission', 100.0, 2, 2, NOW() - INTERVAL '2 days'),
    (4, 8, 'submission', 100.0, 2, 2, NOW() - INTERVAL '2 days'),
    (5, 8, 'submission', 100.0, 2, 2, NOW() - INTERVAL '3 days')
ON CONFLICT (external_id) DO NOTHING;

-- Task 9: Task 0: Practice the Git workflow (5 attempts, 4 passed = 80%)
INSERT INTO interacts (learner_id, item_id, kind, score, checks_passed, checks_total, created_at) VALUES
    (1, 9, 'submission', 100.0, 3, 3, NOW() - INTERVAL '1 day'),
    (2, 9, 'submission', 100.0, 3, 3, NOW() - INTERVAL '1 day'),
    (3, 9, 'submission', 100.0, 3, 3, NOW() - INTERVAL '2 days'),
    (4, 9, 'submission', 100.0, 3, 3, NOW() - INTERVAL '2 days'),
    (5, 9, 'submission', 0.0, 0, 3, NOW() - INTERVAL '3 days')
ON CONFLICT (external_id) DO NOTHING;

-- Task 10: Task 1: Product & architecture description (4 attempts, 2 passed = 50%)
INSERT INTO interacts (learner_id, item_id, kind, score, checks_passed, checks_total, created_at) VALUES
    (1, 10, 'submission', 100.0, 4, 4, NOW() - INTERVAL '1 day'),
    (2, 10, 'submission', 100.0, 4, 4, NOW() - INTERVAL '1 day'),
    (3, 10, 'submission', 25.0, 1, 4, NOW() - INTERVAL '2 days'),
    (4, 10, 'submission', 10.0, 0, 4, NOW() - INTERVAL '2 days')
ON CONFLICT (external_id) DO NOTHING;

-- Insert interactions for lab-02 tasks (parent_id=2, task ids: 17-24)
-- Task 17: Lab setup (5 attempts, 5 passed = 100%)
INSERT INTO interacts (learner_id, item_id, kind, score, checks_passed, checks_total, created_at) VALUES
    (1, 17, 'submission', 100.0, 2, 2, NOW() - INTERVAL '1 day'),
    (2, 17, 'submission', 100.0, 2, 2, NOW() - INTERVAL '1 day'),
    (3, 17, 'submission', 100.0, 2, 2, NOW() - INTERVAL '2 days'),
    (4, 17, 'submission', 100.0, 2, 2, NOW() - INTERVAL '2 days'),
    (5, 17, 'submission', 100.0, 2, 2, NOW() - INTERVAL '3 days')
ON CONFLICT (external_id) DO NOTHING;

-- Task 18: Task 1: Run the web server (5 attempts, 3 passed = 60%)
INSERT INTO interacts (learner_id, item_id, kind, score, checks_passed, checks_total, created_at) VALUES
    (1, 18, 'submission', 100.0, 5, 5, NOW() - INTERVAL '1 day'),
    (2, 18, 'submission', 100.0, 5, 5, NOW() - INTERVAL '1 day'),
    (3, 18, 'submission', 100.0, 5, 5, NOW() - INTERVAL '2 days'),
    (4, 18, 'submission', 0.0, 0, 5, NOW() - INTERVAL '2 days'),
    (5, 18, 'submission', 20.0, 1, 5, NOW() - INTERVAL '3 days')
ON CONFLICT (external_id) DO NOTHING;

-- Insert interactions for lab-04 tasks (parent_id=4, task ids: 32-36)
-- Task 32: Lab setup (5 attempts, 4 passed = 80%)
INSERT INTO interacts (learner_id, item_id, kind, score, checks_passed, checks_total, created_at) VALUES
    (1, 32, 'submission', 100.0, 3, 3, NOW() - INTERVAL '1 day'),
    (2, 32, 'submission', 100.0, 3, 3, NOW() - INTERVAL '1 day'),
    (3, 32, 'submission', 100.0, 3, 3, NOW() - INTERVAL '2 days'),
    (4, 32, 'submission', 50.0, 1, 3, NOW() - INTERVAL '2 days'),
    (5, 32, 'submission', 100.0, 3, 3, NOW() - INTERVAL '3 days')
ON CONFLICT (external_id) DO NOTHING;

-- Task 33: Observe System Component Interaction (5 attempts, 3 passed = 60%)
INSERT INTO interacts (learner_id, item_id, kind, score, checks_passed, checks_total, created_at) VALUES
    (1, 33, 'submission', 100.0, 5, 5, NOW() - INTERVAL '1 day'),
    (2, 33, 'submission', 100.0, 5, 5, NOW() - INTERVAL '1 day'),
    (3, 33, 'submission', 100.0, 5, 5, NOW() - INTERVAL '2 days'),
    (4, 33, 'submission', 0.0, 0, 5, NOW() - INTERVAL '2 days'),
    (5, 33, 'submission', 40.0, 2, 5, NOW() - INTERVAL '3 days')
ON CONFLICT (external_id) DO NOTHING;

-- Task 34: Back-end Testing (5 attempts, 5 passed = 100%)
INSERT INTO interacts (learner_id, item_id, kind, score, checks_passed, checks_total, created_at) VALUES
    (1, 34, 'submission', 100.0, 4, 4, NOW() - INTERVAL '1 day'),
    (2, 34, 'submission', 100.0, 4, 4, NOW() - INTERVAL '1 day'),
    (3, 34, 'submission', 100.0, 4, 4, NOW() - INTERVAL '2 days'),
    (4, 34, 'submission', 100.0, 4, 4, NOW() - INTERVAL '2 days'),
    (5, 34, 'submission', 100.0, 4, 4, NOW() - INTERVAL '3 days')
ON CONFLICT (external_id) DO NOTHING;

-- Task 35: Add Front-end (5 attempts, 2 passed = 40%)
INSERT INTO interacts (learner_id, item_id, kind, score, checks_passed, checks_total, created_at) VALUES
    (1, 35, 'submission', 100.0, 6, 6, NOW() - INTERVAL '1 day'),
    (2, 35, 'submission', 100.0, 6, 6, NOW() - INTERVAL '1 day'),
    (3, 35, 'submission', 20.0, 1, 6, NOW() - INTERVAL '2 days'),
    (4, 35, 'submission', 10.0, 0, 6, NOW() - INTERVAL '2 days'),
    (5, 35, 'submission', 30.0, 2, 6, NOW() - INTERVAL '3 days')
ON CONFLICT (external_id) DO NOTHING;

-- Task 36: Optional CI/CD (2 attempts, 1 passed = 50%)
INSERT INTO interacts (learner_id, item_id, kind, score, checks_passed, checks_total, created_at) VALUES
    (1, 36, 'submission', 100.0, 2, 2, NOW() - INTERVAL '1 day'),
    (2, 36, 'submission', 0.0, 0, 2, NOW() - INTERVAL '1 day')
ON CONFLICT (external_id) DO NOTHING;
