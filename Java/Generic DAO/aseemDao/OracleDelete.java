package aseemDao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;

import aseemEnums.QueryType;
import aseemEnums.TableName;

public class OracleDelete implements DAODelete {
	DAOFactory fac = null;

	public OracleDelete(OracleFactory oracleFactory) {
		fac = oracleFactory;
	}

	@Override
	public <T> boolean deleteFrom(Connection con, TableName tableName,
			T currentPojo) throws SQLException {
		PreparedStatement ps = null;
		try {
			if (fac.getDAORead().<T> alreadyExisting(con, tableName,
					currentPojo) == false) {
				return false;
			}
			String primaryKey = OracleSpecifics.<T> getPrimaryKey(tableName,
					currentPojo);
			ps = con.prepareStatement(OracleSpecifics.queryString(tableName,
					primaryKey, QueryType.DELETE));
			ps.execute();
		} finally {
			DAOFactory.closeAll(ps, null);
		}
		return true;
	}
}
