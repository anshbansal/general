package aseemDao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import aseemEnums.TableName;

public class OracleInsert implements DAOInsert {

	DAOFactory fac = null;

	OracleInsert(OracleFactory oracleFactory) throws SQLException {
		fac = oracleFactory;
	}

	public <T> boolean putInto(Connection con, TableName tableName,
			T currentPojo, boolean running) throws SQLException {
		PreparedStatement ps = null;
		try {
			if (fac.getDAORead().<T> alreadyExisting(con, tableName,
					currentPojo)) {
				return false;
			}
			ps = OracleSpecifics.<T> getPreparedInsert(con, tableName,
					currentPojo, running);
			ps.execute();
			return true;
		} finally {
			DAOFactory.closeAll(ps, null);
		}
	}
}
