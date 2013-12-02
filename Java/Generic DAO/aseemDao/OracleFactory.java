package aseemDao;

import java.sql.SQLException;

public class OracleFactory extends DAOFactory {

	@Override
	public DAOInsert getDAOInsert() throws SQLException {
		return new OracleInsert(this);
	}

	@Override
	public DAORead getDAORead() throws SQLException {
		return new OracleRead(this);
	}

	@Override
	public DAODelete getDAODelete() {
		return new OracleDelete(this);
	}

	@Override
	public DAOUpdate getDAOUpdate() {
		return new OracleUpdate(this);
	}
}
