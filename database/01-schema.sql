CREATE TABLE usuario (
    id_usuario SERIAL PRIMARY KEY,
    uuid_usuario UUID NOT NULL UNIQUE,
    ip_registro VARCHAR(100),
    fecha_registro TIMESTAMP DEFAULT NOW()
);

CREATE TABLE evaluacion (
    id_evaluacion SERIAL PRIMARY KEY,

    id_usuario INT NOT NULL,

    country VARCHAR(100),
    job_role VARCHAR(100),
    ai_specialization VARCHAR(100),
    experience_level VARCHAR(50),
    experience_years INT,
    education_required VARCHAR(100),
    industry VARCHAR(100),
    company_size VARCHAR(50),
    work_mode VARCHAR(50),
    weekly_hours NUMERIC(10,2),

    fecha_evaluacion TIMESTAMP DEFAULT NOW(),

    FOREIGN KEY (id_usuario)
        REFERENCES usuario(id_usuario)
);

CREATE TABLE resultado (
    id_resultado SERIAL PRIMARY KEY,

    id_evaluacion INT NOT NULL,

    future_demand_level VARCHAR(20),
    future_demand_confidence NUMERIC(10,2),

    automation_risk_level VARCHAR(20),
    automation_risk_score NUMERIC(10,2),

    career_growth_level VARCHAR(20),
    career_growth_score NUMERIC(10,2),

    salary_level VARCHAR(20),
    average_salary_usd NUMERIC(12,2),

    similar_profiles_found INT,

    fecha_resultado TIMESTAMP DEFAULT NOW(),

    FOREIGN KEY (id_evaluacion)
        REFERENCES evaluacion(id_evaluacion)
);

CREATE TABLE feedback_chatgpt (
    id_feedback SERIAL PRIMARY KEY,

    id_resultado INT NOT NULL,

    feedback TEXT,

    fecha_generacion TIMESTAMP DEFAULT NOW(),

    FOREIGN KEY (id_resultado)
        REFERENCES resultado(id_resultado)
);

CREATE TABLE historial_consulta (
    id_historial SERIAL PRIMARY KEY,

    id_usuario INT NOT NULL,

    endpoint VARCHAR(100),

    fecha_consulta TIMESTAMP DEFAULT NOW(),

    FOREIGN KEY (id_usuario)
        REFERENCES usuario(id_usuario)
);